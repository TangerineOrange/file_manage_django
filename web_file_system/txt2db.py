
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_file_system.settings")


import django
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()

def main():
    from list.models import Blog
    f = open('oldblog.txt')
    for line in f:
        title,content = line.split('****')
        Blog.objects.create(title=title,content=content)
    f.close()
 
if __name__ == "__main__":
    main()
    print('Done!')