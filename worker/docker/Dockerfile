FROM codeneuro/base

MAINTAINER CodeNeuro <info@codeneuro.org>

USER root

RUN apt-get update

ENV SHELL /bin/bash

# Java setup
RUN apt-get install -y default-jre

# Spark setup 
RUN wget http://d3kbcqa49mib13.cloudfront.net/spark-1.4.1-bin-hadoop1.tgz 
RUN tar -xzf spark-1.4.1-bin-hadoop1.tgz
ENV SPARK_HOME $HOME/spark-1.4.1-bin-hadoop1
ENV PATH $PATH:$SPARK_HOME/bin
RUN sed 's/log4j.rootCategory=INFO/log4j.rootCategory=ERROR/g' $SPARK_HOME/conf/log4j.properties.template > $SPARK_HOME/conf/log4j.properties
ENV _JAVA_OPTIONS "-Xms512m -Xmx4g" 

# Install useful Python packages
RUN apt-get install -y libxrender1 fonts-dejavu && apt-get clean
RUN conda create --yes -q -n python2.7-env python=2.7 nose numpy pandas scikit-learn scikit-image matplotlib scipy seaborn sympy cython patsy statsmodels cloudpickle numba bokeh pillow ipython jsonschema boto
ENV PATH $CONDA_DIR/bin:$PATH
RUN conda install --yes numpy pandas scikit-learn scikit-image matplotlib scipy seaborn sympy cython patsy statsmodels cloudpickle numba bokeh pillow && conda clean -yt
RUN /bin/bash -c "source activate /opt/conda/envs/python2.7-env/ && pip install mistune"

# Thunder setup
RUN apt-get install -y git python-pip ipython gcc
RUN git clone https://github.com/thunder-project/thunder
RUN /bin/bash -c "source activate /opt/conda/envs/python2.7-env/ && pip install -r thunder/requirements.txt"
ENV THUNDER_ROOT $HOME/thunder
ENV PATH $PATH:$THUNDER_ROOT/bin
ENV PYTHONPATH $PYTHONPATH:$THUNDER_ROOT

# Bolt setup
RUN git clone https://github.com/bolt-project/bolt
RUN /bin/bash -c "source activate /opt/conda/envs/python2.7-env/ && pip install -r bolt/requirements.txt"
ENV BOLT_ROOT $HOME/bolt
ENV PYTHONPATH $PYTHONPATH:$BOLT_ROOT

# Configure Boto for S3 access
RUN printf '[s3]\ncalling_format = boto.s3.connection.OrdinaryCallingFormat' >> ~/.boto

RUN git clone https://github.com/CodeNeuro/neurofinder
ENV NEUROFINDER_ROOT $HOME/neurofinder

# Add the notebooks directory
ADD notebooks $HOME/notebooks

# Set up the kernelspec
RUN /opt/conda/envs/python2.7-env/bin/ipython kernelspec install-self

WORKDIR $HOME/notebooks

CMD ipython notebook