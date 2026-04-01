import os
from typing import Any, Optional

from flask import Flask, jsonify, render_template_string, request
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


HTML_TEMPLATE = """
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>ENAE VET – Chatbot simple</title>
  </head>
  <body>
    <h1>Chatbot simple ENAE VET</h1>
    <form method="post" action="/ask_bot">
      <label for="msg">Mensaje:</label>
      <input type="text" id="msg" name="msg" style="width: 300px;" />
      <button type="submit">Enviar</button>
    </form>
  </body>
  </html>
"""


app = Flask(__name__)


def _get_bot_chain() -> Optional[Any]:
    """Build the simplest possible chain: only the user message goes to the LLM.

    No system prompt (no explicit role or instructions). No conversation history.
    """
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return None

    prompt = ChatPromptTemplate.from_messages(
        [
            ("human", "{input}"),
        ]
    )

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.3,
        openai_api_key=api_key,
    )

    return prompt | llm


_bot_chain = _get_bot_chain()


@app.route("/")
def home() -> str:
    """Serve the minimal HTML page for manual testing from a browser."""
    return render_template_string(HTML_TEMPLATE)


@app.route("/ask_bot", methods=["POST"])
def ask_bot():
    """Receive the user message, call the LLM chain, return the reply as JSON."""
    user_msg = (request.form.get("msg") or "").strip()
    if not user_msg:
        return jsonify({"msg": "Please send a non-empty message."}), 400

    if _bot_chain is None:
        return (
            jsonify({"msg": "OPENAI_API_KEY is not set in the environment."}),
            500,
        )

    try:
        response = _bot_chain.invoke({"input": user_msg})
        bot_msg = getattr(response, "content", str(response))
        return jsonify({"msg": bot_msg}), 200
    except Exception as exc:  # noqa: BLE001
        return jsonify({"msg": f"Error: {exc}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

