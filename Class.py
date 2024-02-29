import hashlib

class Member():
    def __init__(self, name, username, password):
        self.name = name.capitalize()
        self.username = username.lower()
        # haslib 라이브러리의 sha256() 함수를 사용하여 비밀번호를 암호화
        self.password = hashlib.sha256(password.encode()).hexdigest()

    def display(self):
        print(f"Name: {self.name}, Username: {self.username}")

class Post(Member):
    def __init__(self, title, content, author):
        self.title = title.lower()
        self.content = content.lower()
        self.author = author

members = []
posts = []

# 회원 인스턴스 3개 생성
for i in range(3):
    # input() 함수를 사용하여 회원 정보를 입력받아 Member 클래스의 인스턴스를 생성
    name = input('Enter name: ')
    username = input('Enter username: ')
    password = input('Enter password: ')
    member = Member(name, username, password)
    members.append(member)

# 회원 정보 출력
for member in members:
    member.display()

# 각 회원별로 게시글 3개씩 생성
for member in members:
    for i in range(3):
        # input() 함수를 사용하여 게시글 정보를 입력받아 Post 클래스의 인스턴스를 생성
        print(f'Enter post for {member.username}')
        title = input('Enter title: ')
        content = input('Enter content: ')
        post = Post(title, content, member.username)
        posts.append(post)

# 특정 멤버의 게시글 출력
member_post = input('Enter username to view posts: ').lower()
for post in posts:
    if post.author == member_post:
        print(post.title)

# 특정 단어가 포함된 게시글 출력
search_word = input('Enter search word: ').lower()
for post in posts:
    if search_word in post.content:
        print(f'{post.title} from {post.author}')