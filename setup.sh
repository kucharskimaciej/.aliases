#/bin/sh
SCRIPTPATH=$( cd $(dirname $0) ; pwd -P  )
git config --global core.excludesfile $SCRIPTPATH/global_ignore

# nvm
sh -c "$(curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.29.0/install.sh)"

apt-get install zsh
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

echo "source \$HOME/.settings/.zshrc" >> ~/.zshrc

apt-get install vim
sh -c "$(curl https://raw.githubusercontent.com/spf13/spf13-vim/3.0/bootstrap.sh -L)"

rm ~/.vimrc.bundles ~/.vimrc.bundles.local ~/.vimrc.local

ln -s $SCRIPTPATH/vim/vimrc ~/.vimrc.local
ln -s $SCRIPTPATH/vim/bundles ~/.vimrc.bundles
ln -s $SCRIPTPATH/vim/bundles ~/.vimrc.bundles.local
