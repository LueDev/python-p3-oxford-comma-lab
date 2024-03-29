def oxford_comma(items):
    if len(items) == 1:
        return "".join(items)
    elif len(items) == 2:
        return " and ".join(items)
    else:
        # concatenate all items that aren't the last with an oxford comma.
        # concatenate the last item with ' and ' 
        return ', '.join(items[:-1]) + f', and {items[-1]}'

if __name__ == "__main__":
    print(oxford_comma(["sex","rock and roll"]))