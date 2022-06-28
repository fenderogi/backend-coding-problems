from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('postgresql://postgres:12345@localhost:5432/SocialMediaCaseStudy')
Session = sessionmaker(bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    full_name = Column(String)
    profile_picture = Column(String)
    bio = Column(String)
    created_at = Column(Integer)

    posts = relationship('Post', backref='user_post')
    likes = relationship('Like', backref='user_like')

    following = relationship(
        'User', lambda: user_following,
        primaryjoin=lambda: User.id == user_following.c.follower_id,
        secondaryjoin=lambda: User.id == user_following.c.following_id,
        backref='followers'
    )


user_following = Table(
    'follow', Base.metadata,
    Column('follower_id', Integer, ForeignKey(User.id), primary_key=True),
    Column('following_id', Integer, ForeignKey(User.id), primary_key=True),
    Column('created_at', Integer)
)


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    image = Column(String)
    created_at = Column(Integer)

    likes = relationship('Like', backref='user')


class Like(Base):
    __tablename__ = 'like'

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    created_at = Column(Integer)


class Follow(Base):
    __tablename__ = 'follow'
    __table_args__ = {'extend_existing': True}

    # id = Column(Integer, primary_key=True)
    follower_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    following_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    created_at = Column(Integer)


Base.metadata.create_all(engine)
session = sessionmaker()(bind=engine)
