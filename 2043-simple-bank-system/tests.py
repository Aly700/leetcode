def run(solution):
    # the LeetCode example
    bank = solution.Bank([10, 100, 20, 50, 30])
    assert bank.withdraw(3, 10) is True
    assert bank.transfer(5, 1, 20) is True
    assert bank.deposit(5, 20) is True
    assert bank.transfer(3, 4, 15) is False
    assert bank.withdraw(10, 50) is False

    # accounts are 1-indexed: 0 and n + 1 are both invalid, n is valid
    single = solution.Bank([7])
    assert single.deposit(0, 1) is False
    assert single.deposit(2, 1) is False
    assert single.deposit(1, 1) is True

    # a failed transfer must leave both balances untouched
    pair = solution.Bank([5, 5])
    assert pair.transfer(1, 2, 6) is False
    assert pair.withdraw(1, 5) is True
    assert pair.withdraw(2, 5) is True

    # invalid destination fails before any money leaves the source
    pair = solution.Bank([5, 5])
    assert pair.transfer(1, 9, 5) is False
    assert pair.withdraw(1, 5) is True

    # withdrawing exactly the balance is allowed, one more is not
    exact = solution.Bank([3])
    assert exact.withdraw(1, 3) is True
    assert exact.withdraw(1, 1) is False

    # transferring to yourself with enough money is a no-op that succeeds
    selfie = solution.Bank([4])
    assert selfie.transfer(1, 1, 4) is True
    assert selfie.withdraw(1, 4) is True
