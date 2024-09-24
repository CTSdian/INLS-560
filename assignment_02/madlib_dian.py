def madlib(adj,adv,n,v):
    story = f'''
    In a distant kingdom, a group of adventurers set off on a perilous journey to find the {adj} artifact said to bring great power.
    They ventured into a dense forest, where the trees seemed to whisper {adv} as they passed.
    After days of traveling, they encountered a {n} guarding the entrance to an ancient temple.
    The group moved carefully, knowing one wrong step could end their quest. With a final {v}, they bypassed the trap and entered the temple, ready to claim their reward.
''' 
    return story

print(
    '''
    In a distant kingdom, a group of adventurers set off on a perilous journey to find the {adj} artifact said to bring great power.
    They ventured into a dense forest, where the trees seemed to whisper {adv} as they passed.
    After days of traveling, they encountered a {n} guarding the entrance to an ancient temple.
    The group moved carefully, knowing one wrong step could end their quest. With a final {v}, they bypassed the trap and entered the temple, ready to claim their reward.
'''
)

print(madlib(input("input the adj:"),input("input the adv:"),input("input the n:"),input("input the v;")))
