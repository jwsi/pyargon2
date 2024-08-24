# pyargon2

Simultaneously the simplest and most powerful implementation of Argon2 in Python.

## Installation 

```bash
pip install pyargon2
```

## Basic Usage

The hash function supports basic password hashing using the Argon2id variant and mandates password and salt strings. The resulting hash returned is hex encoded.

```python
from pyargon2 import hash

password = 'a strong password'
salt = 'a unique salt'
hex_encoded_hash = hash(password, salt)
```

The default parameters aim to generate hashes in around 0.5 seconds and are targeted at a machine housing a CPU with 4 cores and at least 4GB of RAM. If timing differs significantly on your machine, adjust the parameters using the advanced options below.
**Remember password hashing should be slow for security so don't optimise for speed!**

## Advanced Usage

### Function Choices

pyargon2 contains two functions for hashing. Namely, `hash` and `hash_bytes`. These two functions differ in their input types only.
This is explained in detail in the subsequent sections. To minimise input dependent hashing performance, dynamic type checking is not
used in pyargon2. Instead, dedicated functions are exposed to deal with hashing strings or byte arrays separately. As such, one should
ensure that they hash passwords, salts and peppers of the same type and then pick the corresponding function in pyargon2 as
appropriate.

### Function Parameters

The `hash` and `hash_bytes` functions take in the following parameters:

##### Positional

- **password** : A string (or byte array when using `hash_bytes`) representing a password.
- **salt** : A string (or byte array when using `hash_bytes`) representing a unique salt.

##### Keyword (Optional)

- **pepper** : A secret string (or byte array when using `hash_bytes`) to fold into the hash of the password.
- **hash_len** : The length in bytes of the resulting hash.
- **time_cost** : The number of iterations to perform.
- **memory_cost** : The number of kibibytes in memory to utilise.
- **parallelism** : The number of independent computations chains (lanes) to run.
- **flags** : Flags to determine which fields are securely wiped.
- **variant** : Argon2 algorithm variant ('i', 'd', or 'id').
- **version** : Argon2 algorithm version number.
- **encoding** : Encoding for the returned hash type ('raw', 'hex' or 'b64').

For assistance with parameter selection refer to [RFC 9106](https://www.rfc-editor.org/rfc/rfc9106.html), in particular "Chapter 4: Parameter Choice".

### Function Exceptions

Exceptions generated by the underlying Argon2 hashing function are raised under the `Argon2Error` class which can be imported as follows:

```python
from pyargon2 import Argon2Error
```
