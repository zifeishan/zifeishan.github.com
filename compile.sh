set -eu

# make sure in a "website" conda env (with python2 installed)

cd source
scons
cd ..
cp -r source/deploy/* ./
# cd jb
# # jekyll & sleep 2; kill $!
# jekyll build
# cd ..
# cp -r jb/_site/* ./

echo "Finished compiling."
