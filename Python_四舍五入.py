def 四舍五入_法一(float_num: float, ndigits: int = 0) -> float:
    """
    四舍五入_法一: 不准确，例1.035 ❌
    :param float_num: 待四舍五入的浮点数
    :param ndigits: 保留的小数位数
    :return: 四舍五入后的浮点数
    """
    multiplier = 10**ndigits
    return int(float_num * multiplier + 0.5) / multiplier


def 四舍五入_法二(float_num: float, ndigits: int = 0) -> float:
    """
    四舍五入_法二: 不准确，例1.035 ❌
    :param float_num: 待四舍五入的浮点数
    :param ndigits: 保留的小数位数
    :return: 四舍五入后的浮点数
    """
    return round(float_num, ndigits)


def 四舍五入_法三(float_num: float, ndigits: int = 0) -> float:
    """
    四舍五入_法三: 不准确，例1.035 ❌
    :param float_num: 待四舍五入的浮点数
    :param ndigits: 保留的小数位数
    :return: 四舍五入后的浮点数
    """
    return f"{float_num:.{ndigits}f}"


def 四舍五入_法四(float_num: float, ndigits: int = 0) -> float:
    """
    四舍五入_法四: 准确 ✅
    :param float_num: 待四舍五入的浮点数
    :param ndigits: 保留的小数位数
    :return: 四舍五入后的浮点数
    """
    import decimal

    decimal.getcontext().rounding = decimal.ROUND_HALF_UP
    return round(decimal.Decimal(str(float_num)), ndigits)


def 四舍五入_法五(float_num: float, ndigits: int = 0) -> float:
    """
    四舍五入_法五: 准确 ✅
    :param float_num: 待四舍五入的浮点数
    :param ndigits: 保留的小数位数
    :return: 四舍五入后的浮点数
    """
    import decimal

    quantize_exp = decimal.Decimal((0, (1,), -ndigits))
    return decimal.Decimal(str(float_num)).quantize(
        quantize_exp, rounding=decimal.ROUND_HALF_UP
    )


def 四舍五入_测试一() -> None:
    """
    四舍五入_测试一
    :return: None
    """
    a = 1.125
    print(f"{a:.20f}")
    print(四舍五入_法一(a, 2))  # 1.13 ✅
    print(四舍五入_法二(a, 2))  # 1.12 ❌
    print(四舍五入_法三(a, 2))  # 1.12 ❌
    print(四舍五入_法四(a, 2))  # 1.13 ✅
    print(四舍五入_法五(a, 2))  # 1.13 ✅

    a = 1.035
    print(f"{a:.20f}")
    print(四舍五入_法一(a, 2))  # 1.03 ❌
    print(四舍五入_法二(a, 2))  # 1.03 ❌
    print(四舍五入_法三(a, 2))  # 1.03 ❌
    print(四舍五入_法四(a, 2))  # 1.04 ✅
    print(四舍五入_法五(a, 2))  # 1.04 ✅

    print()

    for j in range(1, 3):
        for i in range(1, 10**j):
            s = f"1.{i:0{j}}4"
            a = float(s)
            print(
                f"s={s}, a={a:.20f}, 四舍五入_法四={四舍五入_法四(a, j)}, 四舍五入_法五={四舍五入_法五(a, j)}"
            )

    print()

    for j in range(1, 3):
        for i in range(1, 10**j):
            s = f"1.{i:0{j}}5"
            a = float(s)
            print(
                f"s={s}, a={a:.20f}, 四舍五入_法四={四舍五入_法四(a, j)}, 四舍五入_法五={四舍五入_法五(a, j)}"
            )

    print()

    for j in range(1, 3):
        for i in range(1, 10**j):
            s = f"1.{i:0{j}}6"
            a = float(s)
            print(
                f"s={s}, a={a:.20f}, 四舍五入_法四={四舍五入_法四(a, j)}, 四舍五入_法五={四舍五入_法五(a, j)}"
            )


if __name__ == "__main__":
    四舍五入_测试一()
