# build.sh
#pip install pipenv
echo "🔨 - Starting build"
cd notion
#pipenv install
echo "📄 - Get posts"
#pipenv shell
#pipenv run python get_blog_posts.py
python get_blog_posts.py
cd ..
echo "🦖 - Build frontend site"
npm install
npm run build

#gatsby develop

# netlify.toml
#[build]
#  publish = "public/"
  # Default build command.
#  command = "bash build.sh"
# runtime.txt
#3.7