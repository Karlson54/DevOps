import fire
import utils

if __name__ == "__main__":
    fire.Fire({
        "greet": utils.greet,
        "goodbye": utils.goodbye
    })
