print('hello world')

def test_debugging(b: int, a: int):

    for i in range(b):
        a = a + i
    return a
print(test_debugging(10, 2))


print('test_branch_1')
print('test_branch_1_second_change')

# Revert brings back the commit.
# You can merge branch to the master in the github side or here in pycharm
# If you merge the master in the github side, then you can pull the master here

# If you have done any changes first commit it and then do another action such as pull otr merge .