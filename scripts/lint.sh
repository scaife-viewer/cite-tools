#!/bin/bash
isort -rc cite_tools
black cite_tools
flake8 cite_tools
