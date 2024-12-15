import os
import argparse

from json import loads
from typing import Dict
from shutil import rmtree
from textwrap import dedent


def adapter_test_go(data: Dict[str, str]) -> str:
    return dedent(f"""
        package main

        import (
            "github.com/gonebot-dev/gonebot"
            {data["adapter"].split('.')[0]} "{data["package"]}"
            echo "github.com/gonebot-dev/goneplugin-echo"
        )

        func main() {{
            gonebot.LoadPlugin(&echo.Echo)
            gonebot.LoadAdapter(&{data["adapter"]})
            gonebot.Run()
        }}
    """)


def plugin_test_go(data: Dict[str, str]) -> str:
    return dedent(f"""
        package main

        import (
            onebotv11 "github.com/gonebot-dev/goneadapter-onebotv11"
            "github.com/gonebot-dev/gonebot"
            {data["plugin"].split('.')[0]} "{data["package"]}"
        )

        func main() {{
            gonebot.LoadPlugin(&{data["plugin"]})
            gonebot.LoadAdapter(&onebotv11.OneBotV11)
            gonebot.Run()
        }}
    """)


if __name__ == "__main__":
    # Get json file path from command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("json_path", help="Path to the JSON file", type=str)
    json_path: str = parser.parse_args().json_path
    json_path = json_path.replace("\\", "/")
    if not json_path.endswith(".json"):
        print(f"{json_path} is not a valid JSON file!")
        exit(1)

    # Read the JSON file
    with open(json_path, "r") as json_file:
        data: Dict[str, str] = loads(json_file.read())

    # Generate the test file
    is_adapter = json_path.startswith("packages/adapters")
    if not is_adapter and not json_path.startswith("packages/plugins"):
        print(f"{json_path} is not a valid JSON file for adapter or plugin!")
        exit(1)
    if os.path.exists("test/"):
        rmtree("test/")
    os.mkdir("test/")
    with open("test/.env", "w") as env_file:
        env_file.write(dedent("""
            COMMAND_START="/"
            NICKNAME="bot"
            LOG_LEVEL="INFO"

            ONEBOTV11_HOST="127.0.0.1:21390"
        """))
    with open("test/main.go", "w") as go_file:
        go_file.write(
            adapter_test_go(data) if is_adapter
            else plugin_test_go(data)
        )
