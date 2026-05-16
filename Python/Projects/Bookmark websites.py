MyFavouriteList = []
MaximumBookmarks = 5
while 0 < MaximumBookmarks:
    MyFavouriteListInput = input('Please enter your favourite website https://: ')
    MyFavouriteList.append(MyFavouriteListInput)
    MaximumBookmarks -= 1
else:
    print('You have reached the maximum number of bookmarks.')
    print('Your favourite websites are:')
    for website in MyFavouriteList:
        print(f"https://{website}")