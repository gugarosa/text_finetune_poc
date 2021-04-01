# Proof-of-Concept with Roncarati

*This repository holds all the necessary code to run the discontinued proof-of-concept from Roncarati. Note that data is private and will not be available.*

---

## Installation

### Starting MySQL with Docker

To ease one needs in a development environment, we ship MySQL in a Docker container. Make sure that ```docker``` and ```docker-compose``` are installed and accessible from the command line.

Finally, you can build the container by using:

```
docker-compose build
```

After the build process is finished, you can run the container in detached mode:

```
docker-compose up -d
```

If you ever need to perform maintenance or update the repository, please put the container down (ensure to use -v; otherwise it will not replace the build):

```
docker-compose down
```
### Initializing a Python Environment

Install all the pre-needed requirements using:

```Python
pip install -r requirements.txt
```

---

## Usage

### (Optional) Connect to MySQL Database

The first step is to test whether the connection to the MySQL database is working. To accomplish such a procedure, please use the following script:

```Python
python connect_mysql.py
```

*Remember to check if the host, username, password and database are the ones initialized by the Docker container.*

### Query and Dump Data

One of the most important parts of this PoC is that we need to query the desired data and dump it to a `.csv` file, as follows:

```Python
python query_data.py
```

*Note that you need to supply the query and use it accordingly to the data that should be dumped.*

### Classify the Data

Finally, we can now gather a pre-trained Transformer and fine-tune the architecture using the data we have just dumped. The following script performs such a procedure:

```Python
python classify_data.txt
```

*We are using [Textfier](https://github.com/gugarosa/textfier) as our engine, which is basically a wrapper around Huggingface's Transformers library.

---

## Environment Configuration

Note that sometimes, there is a need for additional implementation. If needed, from here, you will be the one to know all of its details.

### Ubuntu

No specific additional commands needed.

### Windows

No specific additional commands needed.

### MacOS

No specific additional commands needed.

---

## Support

We know that we do our best, but it is inevitable to acknowledge that we make mistakes. If you ever need to report a bug, report a problem, talk to us, please do so! We will be available at our bests at this repository or gustavo.rosa@unesp.br.

---
