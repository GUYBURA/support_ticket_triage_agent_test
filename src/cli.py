from src.config import get_llm


def main() -> None:
    llm = get_llm()
    print(llm.invoke("Say hi in 3 words.").content)


if __name__ == "__main__":
    main()
