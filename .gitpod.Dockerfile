FROM gitpod/workspace-full
USER gitpod
RUN sudo apt-get update && sudo apt-get install -y zsh && \
    wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh && \
    rm -rf install.sh

RUN pyenv install 3.10.5 && \
    pyenv global 3.10.5