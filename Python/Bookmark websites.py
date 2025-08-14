MyFavouriteList = []
MaximumBookmarks = 3
while 0 < MaximumBookmarks:
    MyFavouriteListInput = input('Please enter your favourite website (https://): ')
    MyFavouriteList.append(MyFavouriteListInput)
    MaximumBookmarks -= 1
else:
    print('You have reached the maximum number of bookmarks.')
    print(f'Your favourite websites are: {MyFavouriteList.lower()}')