cd source
scons
cd ..
cp -r source/deploy/* ./
cd jb
jekyll & sleep 2; kill $!
cd ..
cp -r jb/_site/* ./
