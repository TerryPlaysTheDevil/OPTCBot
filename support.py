from OPTCBot import config as c


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def botHasNotAnswered(comment):
    for reply in comment.replies:
        if reply.author.name == "OPTCBot":
            return False
    return True


def decideSubreddit(subreddit):
    if subreddit == "OnePieceTC":
        return c.FLAIR_FLAIR_MISSING_MESSAGE_OPTC
    elif subreddit == "NarutoBlazing":
        return c.FLAIR_FLAIR_MISSING_MESSAGE_NARUTO
        # elif subreddit == "XXX":
        #    return (FLAIR_FLAIR_MISSING_MESSAGE_XXX)
    else:
        # subreddit could not be identified for some reason, eg trouble with the API, I'd recommend to have a default
        return c.FLAIR_FLAIR_MISSING_MESSAGE_DEFAULT
