#!/usr/bin/env python

from fastapi import FastAPI, Path
import time

import prime_numbers as pn

app = FastAPI()


@app.get("/")
def root():
    return {"message": "hello world"}

@app.get("/ping")
def pong():
    return {"ping": "pong!"}

limit = 10000000

@app.get("/prime/{n}")
def get_primes(*, n: int=Path(..., title='limit upto which prime numbers are required', ge=1, le=limit)):
    then = time.process_time()
    pns = pn.gen_prime_numbers(n)
    duration = time.process_time() - then
    return { "inputNumber": n, "primeCount": len(pns), "durationSeconds": duration, "primeNumbers": pns[-1000:] }

