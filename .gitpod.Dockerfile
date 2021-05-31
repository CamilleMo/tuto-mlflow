FROM gitpod/workspace-full:latest
USER gitpod
RUN sudo apt-get update && sudo apt-get install -y zsh && \
    wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh && \
    rm -rf install.sh

 ENV PATH /opt/conda/bin:$PATH
 ENV MLFLOW_TRACKING_URI http://localhost:5000

 RUN sudo wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-py38_4.9.2-Linux-x86_64.sh -O miniconda.sh && \
     sudo mkdir -p /opt && \
     sudo sh miniconda.sh -b -p /opt/conda && \
     sudo rm miniconda.sh && \
     sudo ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
     # echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
     # echo "conda activate base" >> ~/.bashrc && \
     sudo find /opt/conda/ -follow -type f -name '*.a' -delete && \
     sudo find /opt/conda/ -follow -type f -name '*.js.map' -delete && \
     sudo /opt/conda/bin/conda clean -afy && \
     sudo chmod -R 777 /opt
