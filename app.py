import asyncio
from quart import Quart, request, Response
from quart_cors import cors

import subprocess

app = Quart(__name__)
app = cors(app)

async def run_apt_update():
    process = await asyncio.create_subprocess_exec(
        "sh","test.py",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    async for line in process.stdout:
        print(line.decode())
        yield line.decode()


@app.route("/update")
async def update():
    if "text/event-stream" not in request.headers.get("Accept"):
        return "This endpoint is intended for EventSource (SSE) connections only.", 400

    response_headers = {
        "Content-Type": "text/event-stream",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
    }

    response = Response(generate(), headers=response_headers)
    response.timeout = None
    return response


async def generate():
    async for line in run_apt_update():
        yield f"data: {line}\n\n"


if __name__ == "__main__":
    app.run()
