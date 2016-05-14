#!/usr/bin/python
# -*- coding: utf-8 -*-

import httplib
import json

def main():
  # Establishes an HTTP connection with the local Idibon Public server
  connection = httplib.HTTPConnection("localhost:8080")

  content = "this is a sample string"

  body = json.dumps({"content": content, "features": "true", "feature_threshold": 0.55, "metadata": "true"})

  # Sends a GET request to the server for the English Social Sentiment model
  connection.request("GET", "/NewsWire_Relevance/ConsumerElectronics", body)
  response = connection.getresponse()
  res = response.read()

  # Formats the prediction from the Idibon Public server to print
  json_res = json.loads(res[1:-1])

  # Ensure the classification matches
  print json.dumps(json_res, sort_keys = True, indent = 4, separators = (',', ': '))

  # Closes the HTTP connection
  connection.close()

  return


main()

