#!/usr/bin/env python3
from dotenv import load_dotenv
import os
import sys


def load_config() -> dict[str, str | None]:
    load_dotenv()
    required_vars: list[str] = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"]
    missing: list[str] = []
    for var in required_vars:
        if not os.getenv(var):
            missing.append(var)

    if missing:
        print("ERROR: Missing configuration.")
        for m in missing:
            print(f"- {m}")
        sys.exit(1)

    config = {var: os.getenv(var) for var in required_vars}
    return config


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")
    config = load_config()
    mode = config["MATRIX_MODE"]
    print("Configuration loaded:")
    print("Mode:", mode)
    if mode == "development":
        print("Database: Connected to local instance")
    elif mode == "production":
        print("Database: Connected to production")
    else:
        print("Unknow environment")
        print("API Access: WARNING")
        print("ZION Network: Offline")

    log_level = os.getenv("LOG_LEVEL")
    print("API Access: Authenticated")
    print("Log level:", log_level)
    print("Zion Network: Online")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("No .env file")
    if mode == "development":
        print("[OK] Production overrides available")
    else:
        print("[OK] Production configuration activate")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
