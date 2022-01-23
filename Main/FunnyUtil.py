from shareka_v4 import Shareka

class FunnyUtil:
    def JudgeFunny(text: str) -> int:
        if Shareka(text).dajarewake():
            return 1
        return 0