set -eu

cd source
scons
cd ..
cp -r source/deploy/* ./
cd jb
# jekyll & sleep 2; kill $!
jekyll build
cd ..
cp -r jb/_site/* ./

echo "Finished compiling."
