# 0. Basics of HTTP/HTTPS

**Background:**
The Hypertext Transfer Protocol (HTTP) is the foundation of data communication on the web. It allows web clients (like browsers) to communicate with web servers. HTTP has evolved over time and has a secure counterpart called HTTPS (HTTP Secure). HTTPS is just like HTTP but with an added layer of security using SSL/TLS encryption. This layer protects the data from eavesdroppers and tampering.

**Objective:**
At the end of this exercise, students should be able to:
* Differentiate between HTTP and HTTPS.
* Understand the basic working and structure of HTTP requests and responses.
* Recognize and explain the common HTTP methods and status codes.

---

## Instructions

### Differentiating HTTP and HTTPS

1.  **Read the provided resources:** Familiarize yourself with the basic differences between HTTP and HTTPS using the given links (MDN, Difference between HTTP and HTTPS).
2.  **Identify key differences:** Note down the main distinctions, focusing on security aspects.
    * **HTTP:** Not secure, data is unencrypted (visible to third parties).
    * **HTTPS:** Secure, uses SSL/TLS for encryption (protects against eavesdropping and tampering).
    * **Default Port:** HTTP uses port 80, HTTPS uses port 443.
    * **SSL/TLS Certificate:** HTTPS requires an SSL/TLS certificate for authentication and encryption.
3.  **Expected Output:** Write a brief summary explaining these differences, emphasizing the security aspects.

### Understanding HTTP Structure

1.  **Open Developer Tools:**
    * Open your web browser (Chrome, Firefox, Edge, etc.).
    * Visit a simple website (e.g., `https://www.example.com`).
    * Right-click anywhere on the page and select "Inspect" or "Inspect Element".
    * Navigate to the "Network" tab.
2.  **Observe a Request:**
    * Reload the page if the "Network" tab is empty.
    * You'll see a list of all requests made by the page.
    * Click on the first request (usually the request for the HTML page itself, with a 200 status).
3.  **Analyze Headers:**
    * In the request details panel (often labeled "Headers"), examine the following sections:
        * **Request URL:** The URL of the requested resource.
        * **Request Method:** The HTTP method used (e.g., GET).
        * **Status Code:** The status code of the response (e.g., 200 OK).
        * **Request Headers:** Information sent by the client (your browser) to the server.
        * **Response Headers:** Information sent by the server to the client.
4.  **Expected Output:** Depict or outline the structure of an HTTP request and response. Mention key elements such as method, path, status codes, and headers.

### Exploring HTTP Methods and Status Codes

1.  **List of HTTP Methods:**
    * Based on the provided resources, list at least **four** common HTTP methods.
    * For each method, include:
        * **Method Name:** (e.g., GET)
        * **Description:** What the method does.
        * **Use Case:** A scenario where this method would be used.
    * Common examples include: GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS.
2.  **List of HTTP Status Codes:**
    * Using the "List of HTTP status codes" resource, list at least **five** common HTTP status codes.
    * For each code, include:
        * **Status Code:** (e.g., 404)
        * **Description:** What the code signifies.
        * **Scenario:** An example situation where this status code might be encountered.
    * Ensure you cover different categories (1xx, 2xx, 3xx, 4xx, 5xx).

---

## Expected Output Summary

Your final submission should include:

* A **brief summary** explaining the differences between HTTP and HTTPS.
* A **depiction or outline** of the structure of an HTTP request and response.
* **Two distinct lists:**
    * A list of common **HTTP methods** with their descriptions and possible use cases (at least 4).
    * A list of common **HTTP status codes** with their descriptions and scenarios where they might be encountered (at least 5).
