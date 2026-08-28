#!/bin/sh
ollama serve &
sleep 5
ollama pull mollm2:135m
wait

 