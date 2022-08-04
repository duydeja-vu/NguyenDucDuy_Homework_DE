from http.client import UNAUTHORIZED

# The requested action was successful
OK = 200

# A new resource was created
CREATED = 201

# The request was received, but no modification has been made yet
ACCEPTED = 202

# The request was successful, but the response has no content
NO_CONTENT = 204

# The request was malformed
BAD_REQUEST = 400

# The client is not authorized to perform the requested action
UNAUTHORIZED = 401

# The requested resource was not found
NOT_FOUND = 404

# The request data format is not supported by the server
UNSUPPORTED_MEDIA_TYPE = 415
# The request data was properly formatted but contained invalid or missing data
UNPROCESSABLE_ENTITY = 422

# The server threw an error when processing the request
INTERNAL_SERVER_ERROR = 500
