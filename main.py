def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("--- 前処理 ---")
        result = func(*args, **kwargs)
        print("--- 後処理 ---")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"こんにちは、{name}さん！")
