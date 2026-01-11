from models.meme import Meme
from models.meme_image import MemeImage
from models.meme_source import MemeSource

memes = [
    Meme(
        id=1,
        description="Always creative",
        image=MemeImage(
            url="https://i.chzbgr.com/full/10562962176/h3DF892FA/dev-creates-simple-and-intuitive-ui-user"
        ),
        source=MemeSource.DEVS,
    ),
    Meme(
        id=2,
        description="Look at Code I Wrote Last Year",
        image=MemeImage(
            url="https://i.chzbgr.com/full/10562963968/hF0770D4B/look-at-code-wrote-last-year-why-why-n-imgflipcom-why-oh-s-why"
        ),
        source=MemeSource.DEVS,
    ),
    Meme(
        id=3,
        description="Always improving",
        image=MemeImage(
            url="https://i.chzbgr.com/full/10562966272/h8346A8D3/hires-another-designer-engineers-company-hires-another-engineer-am-not-enough-apes-together-strong"
        ),
        source=MemeSource.DEVS,
    ),
    Meme(
        id=4,
        description="Always adapting",
        image=MemeImage(
            url="https://i.chzbgr.com/full/10562966528/hF0E40B8F/cat-width-100-height-100-1234"
        ),
        source=MemeSource.DEVS,
    ),
    Meme(
        id=5,
        description="Always collaborating",
        image=MemeImage(
            url="https://www.globalnerdy.com/wp-content/uploads/2025/08/bad-day-at-work.jpg"
        ),
        source=MemeSource.DEVS,
    ),
    Meme(
        id=6,
        description="Debugging life",
        image=MemeImage(
            url="https://www.globalnerdy.com/wp-content/uploads/2025/08/6-hours-of-debugging.jpeg"
        ),
        source=MemeSource.DEVS,
    ),
    Meme(
        id=7,
        description="I see something else",
        image=MemeImage(
            url="https://www.globalnerdy.com/wp-content/uploads/2025/08/dishwasher-tablet-or-python-icon.jpeg"
        ),
        source=MemeSource.DEVS,
    ),
    Meme(
        id=8,
        description="We are here to replace you",
        image=MemeImage(
            url="https://www.globalnerdy.com/wp-content/uploads/2025/08/here-to-replace-you.jpg"
        ),
        source=MemeSource.DEVS,
    ),
]
