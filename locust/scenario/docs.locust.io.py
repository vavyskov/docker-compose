from locust import task, run_single_user
from locust import FastHttpUser


class docs_locust_io(FastHttpUser):
    host = "https://docs.locust.io"
    default_headers = {
        "Accept-Language": "cs,sk;q=0.8,en-US;q=0.5,en;q=0.3",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
    }

    @task
    def t(self):
        with self.client.request(
            "GET",
            "/en/stable/",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500606.0.0.0",
                "Host": "docs.locust.io",
                "If-Modified-Since": "Mon, 23 Dec 2024 08:41:29 GMT",
                "If-None-Match": 'W/"f7cc6c9f4923efa09295cf043029ce05"',
                "Priority": "u=0, i",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://www.googletagmanager.com/gtag/js?id=G-MCG99XYF9M",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.googletagmanager.com",
                "Connection": "keep-alive",
                "Host": "www.googletagmanager.com",
                "Referer": "https://docs.locust.io/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/_static/theme-overrides.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500616.0.0.0",
                "Host": "docs.locust.io",
                "Priority": "u=2",
                "Referer": "https://docs.locust.io/en/stable/",
                "Sec-Fetch-Dest": "style",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/_static/css/rtd_sphinx_search.min.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500616.0.0.0",
                "Host": "docs.locust.io",
                "Priority": "u=2",
                "Referer": "https://docs.locust.io/en/stable/",
                "Sec-Fetch-Dest": "style",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/jquery.js?v=5d32c60e",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500616.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/_sphinx_javascript_frameworks_compat.js?v=2cd50e6c",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500616.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/documentation_options.js?v=f9bd780e",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500616.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/doctools.js?v=9a2dae69",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500616.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/sphinx_highlight.js?v=dc90522c",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500616.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/js/rtd_search_config.js",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500616.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/js/rtd_sphinx_search.min.js",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500616.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/js/theme.js",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500616.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_/static/javascript/readthedocs-addons.js",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500616.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500616.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/_/addons/?client-version=0.23.2&api-version=1&project-slug=locust&version-slug=stable",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500616.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/what-is-locust.html",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500616.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Purpose": "prefetch",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_/api/v2/analytics/?project=locust&version=stable&absolute_uri=https%3A%2F%2Fdocs.locust.io%2Fen%2Fstable%2F",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500616.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://media.ethicalads.io/media/client/ethicalads.min.js",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Connection": "keep-alive",
                "Host": "media.ethicalads.io",
                "Referer": "https://docs.locust.io/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/what-is-locust.html",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500616.0.0.0",
                "Host": "docs.locust.io",
                "Priority": "u=0, i",
                "Referer": "https://docs.locust.io/en/stable/",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "TE": "trailers",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://www.googletagmanager.com/gtag/js?id=G-MCG99XYF9M",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.googletagmanager.com",
                "Connection": "keep-alive",
                "Host": "www.googletagmanager.com",
                "Referer": "https://docs.locust.io/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/_static/theme-overrides.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500616.0.0.0",
                "Host": "docs.locust.io",
                "Priority": "u=2",
                "Referer": "https://docs.locust.io/en/stable/what-is-locust.html",
                "Sec-Fetch-Dest": "style",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/_static/css/rtd_sphinx_search.min.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500616.0.0.0",
                "Host": "docs.locust.io",
                "Priority": "u=2",
                "Referer": "https://docs.locust.io/en/stable/what-is-locust.html",
                "Sec-Fetch-Dest": "style",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/jquery.js?v=5d32c60e",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500616.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/what-is-locust.html",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/_sphinx_javascript_frameworks_compat.js?v=2cd50e6c",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500616.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/what-is-locust.html",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/documentation_options.js?v=f9bd780e",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500616.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/what-is-locust.html",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/doctools.js?v=9a2dae69",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500616.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/what-is-locust.html",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/sphinx_highlight.js?v=dc90522c",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500616.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/what-is-locust.html",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/js/rtd_search_config.js",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500616.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/what-is-locust.html",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/js/rtd_sphinx_search.min.js",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500616.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/what-is-locust.html",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/js/theme.js",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500616.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/what-is-locust.html",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_/static/javascript/readthedocs-addons.js",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500616.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/what-is-locust.html",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://www.youtube.com/embed/Ok4x2LIbEEY?start=163&end=1477;",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.youtube.com",
                "Connection": "keep-alive",
                "Cookie": "YSC=Dp9xiJrpawI; VISITOR_INFO1_LIVE=89i2pPImQMo; VISITOR_PRIVACY_METADATA=CgJDWhIcEhgSFhMLFBUWFwwYGRobHB0eHw4PIBAREiEgWA%3D%3D; __Secure-ROLLOUT_TOKEN=CNfl3LOVhpawAhCa9J682s2KAxia9J682s2KAw%3D%3D",
                "Host": "www.youtube.com",
                "Priority": "u=4",
                "Referer": "https://docs.locust.io/",
                "Sec-Fetch-Dest": "iframe",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500616.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/what-is-locust.html",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://www.youtube.com/s/player/03dbdfab/player_ias.vflset/cs_CZ/embed.js",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.youtube.com",
                "Connection": "keep-alive",
                "Cookie": "YSC=Dp9xiJrpawI; VISITOR_INFO1_LIVE=89i2pPImQMo; VISITOR_PRIVACY_METADATA=CgJDWhIcEhgSFhMLFBUWFwwYGRobHB0eHw4PIBAREiEgWA%3D%3D; __Secure-ROLLOUT_TOKEN=CNfl3LOVhpawAhCa9J682s2KAxia9J682s2KAw%3D%3D",
                "Host": "www.youtube.com",
                "Priority": "u=1",
                "Referer": "https://www.youtube.com/embed/Ok4x2LIbEEY?start=163&end=1477;",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://www.youtube.com/s/player/03dbdfab/www-embed-player.vflset/www-embed-player.js",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.youtube.com",
                "Connection": "keep-alive",
                "Cookie": "YSC=Dp9xiJrpawI; VISITOR_INFO1_LIVE=89i2pPImQMo; VISITOR_PRIVACY_METADATA=CgJDWhIcEhgSFhMLFBUWFwwYGRobHB0eHw4PIBAREiEgWA%3D%3D; __Secure-ROLLOUT_TOKEN=CNfl3LOVhpawAhCa9J682s2KAxia9J682s2KAw%3D%3D",
                "Host": "www.youtube.com",
                "Referer": "https://www.youtube.com/embed/Ok4x2LIbEEY?start=163&end=1477;",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://www.youtube.com/s/player/03dbdfab/player_ias.vflset/cs_CZ/base.js",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.youtube.com",
                "Connection": "keep-alive",
                "Cookie": "YSC=Dp9xiJrpawI; VISITOR_INFO1_LIVE=89i2pPImQMo; VISITOR_PRIVACY_METADATA=CgJDWhIcEhgSFhMLFBUWFwwYGRobHB0eHw4PIBAREiEgWA%3D%3D; __Secure-ROLLOUT_TOKEN=CNfl3LOVhpawAhCa9J682s2KAxia9J682s2KAw%3D%3D",
                "Host": "www.youtube.com",
                "Referer": "https://www.youtube.com/embed/Ok4x2LIbEEY?start=163&end=1477;",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/_/addons/?client-version=0.23.2&api-version=1&project-slug=locust&version-slug=stable",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500616.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/what-is-locust.html",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_/api/v2/analytics/?project=locust&version=stable&absolute_uri=https%3A%2F%2Fdocs.locust.io%2Fen%2Fstable%2Fwhat-is-locust.html",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500633.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/what-is-locust.html",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://media.ethicalads.io/media/client/ethicalads.min.js",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Connection": "keep-alive",
                "Host": "media.ethicalads.io",
                "Referer": "https://docs.locust.io/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://googleads.g.doubleclick.net/pagead/id",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "googleads.g.doubleclick.net",
                "Connection": "keep-alive",
                "Host": "googleads.g.doubleclick.net",
                "Origin": "https://www.youtube.com",
                "Referer": "https://www.youtube.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://static.doubleclick.net/instream/ad_status.js",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "static.doubleclick.net",
                "Connection": "keep-alive",
                "Host": "static.doubleclick.net",
                "If-Modified-Since": "Thu, 12 Dec 2013 23:40:16 GMT",
                "Referer": "https://www.youtube.com/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://jnn-pa.googleapis.com/$rpc/google.internal.waa.v1.Waa/Create",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Connection": "keep-alive",
                "Content-Length": "24",
                "Content-Type": "application/json+protobuf",
                "Host": "jnn-pa.googleapis.com",
                "Origin": "https://www.youtube.com",
                "Referer": "https://www.youtube.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "X-Goog-Api-Key": "AIzaSyDyT5W0Jh49F30Pqqtyfdf7pDLFKLJoAnw",
                "X-User-Agent": "grpc-web-javascript/0.1",
            },
            data='["O43z0dpjhgX20SCx4KAo"]',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://www.youtube.com/s/player/03dbdfab/player_ias.vflset/cs_CZ/remote.js",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.youtube.com",
                "Connection": "keep-alive",
                "Cookie": "YSC=Dp9xiJrpawI; VISITOR_INFO1_LIVE=89i2pPImQMo; VISITOR_PRIVACY_METADATA=CgJDWhIcEhgSFhMLFBUWFwwYGRobHB0eHw4PIBAREiEgWA%3D%3D; __Secure-ROLLOUT_TOKEN=CNfl3LOVhpawAhCa9J682s2KAxia9J682s2KAw%3D%3D",
                "Host": "www.youtube.com",
                "Referer": "https://www.youtube.com/embed/Ok4x2LIbEEY?start=163&end=1477;",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://www.google.com/js/th/WuArCo6uiOC32QOIiNWeSH9h2H5vf_jv_ihZ0ZQebSo.js",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.google.com",
                "Connection": "keep-alive",
                "Host": "www.google.com",
                "Referer": "https://www.youtube.com/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "https://googleads.g.doubleclick.net/pagead/id?slf_rd=1",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "googleads.g.doubleclick.net",
                "Connection": "keep-alive",
                "Host": "googleads.g.doubleclick.net",
                "Origin": "https://www.youtube.com",
                "Referer": "https://www.youtube.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://www.youtube.com/generate_204?OIjQww",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.youtube.com",
                "Connection": "keep-alive",
                "Cookie": "YSC=Dp9xiJrpawI; VISITOR_INFO1_LIVE=89i2pPImQMo; VISITOR_PRIVACY_METADATA=CgJDWhIcEhgSFhMLFBUWFwwYGRobHB0eHw4PIBAREiEgWA%3D%3D; __Secure-ROLLOUT_TOKEN=CNfl3LOVhpawAhCa9J682s2KAxia9J682s2KAw%3D%3D",
                "Host": "www.youtube.com",
                "Priority": "u=5, i",
                "Referer": "https://www.youtube.com/embed/Ok4x2LIbEEY?start=163&end=1477;",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/installation.html",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500633.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/what-is-locust.html",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Purpose": "prefetch",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://play.google.com/log?format=json&hasfast=true&authuser=0",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "play.google.com",
                "Connection": "keep-alive",
                "Content-Length": "426",
                "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
                "Host": "play.google.com",
                "Origin": "https://www.youtube.com",
                "Referer": "https://www.youtube.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
                "X-Goog-AuthUser": "0",
            },
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"cs",null,"41",null,null,[1,0,0,0,0]]],1828,[["1735500635064",null,null,null,null,null,null,"[[[\\"/client_streamz/bg/ec\\",null,[\\"en\\",\\"mk\\"],[[[[\\"t\\"],[\\"aGIf\\"]],[1]]]],[\\"/client_streamz/bg/el\\",null,[\\"en\\",\\"rk\\",\\"mk\\"],[[[[\\"t\\"],[\\"\\"],[\\"aGIf\\"]],[null,388]]]]]]",null,null,null,null,null,null,-3600,null,null,null,null,null,1]],"1735500635065"]',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://jnn-pa.googleapis.com/$rpc/google.internal.waa.v1.Waa/GenerateIT",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Connection": "keep-alive",
                "Content-Length": "976",
                "Content-Type": "application/json+protobuf",
                "Host": "jnn-pa.googleapis.com",
                "Origin": "https://www.youtube.com",
                "Referer": "https://www.youtube.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
                "X-Goog-Api-Key": "AIzaSyDyT5W0Jh49F30Pqqtyfdf7pDLFKLJoAnw",
                "X-User-Agent": "grpc-web-javascript/0.1",
            },
            data='["O43z0dpjhgX20SCx4KAo","$X8A5wJhRAAbV9Q9H9fXeL4oHfcbPmB2nADQBEArZ1FFYUrzmU1mIRsV4s15Lsi1jh4EmxrYTjpW7nBI7GnKnZtk9-leGvkhwEM9nQdvnngAAANPOAAAAA_QBB-IAEuyTLBHTiqumom0BzbA5y9xZ5pYBHo-OyocrPgDux7IeRZ7vQWqjn1LpDfkWpc7AQd40BbLSULbdxXVe2-NYF5ldiGWFoCjD-w3K9PWUETRGzgO5nTZ6kjDGe6GQImVOoGparLSw6a-2kMQBkKGbjex86n8VCMW1GCBSAGhUqIaHvsqqPpC2uVGTRVSPSWqyDlHoOEOFersCq6jECM5GvY4uFQqtiDlW4ScGbm29wpBHg6cNbRIGjQ-4O3peN3hqkddSzI5LTYGlXR2ORG14v2WRslIjuQA668S_BHpB5VvRdtFYkUVRvfSAFiXDyaT7u7JcPuTvOAqNqQlk4tjtyViuEo0L_Ok0S6XdUk8CWqG8pXWWTYdhrZo9FXqnywEziyL9wNQd5uFef-zQ5fCsdQfb3B0FATNgBZsoSRRujcqyc5-m3QONjHGGaBWKfJL-4N0kHZNQMgNAzuHjfKlP7gUFP5zpXrfXmcWd7CgyckAaZr9OlSz7hs4HWSX2BelgN7z1mLJEj5kzJeJhl8vks4BiDJSUpQnLW7IdCru2X1gTEwFXGDnSSeqSCjaz35JQQNGh4b9vuFsrqVDMtwLhjPLjEFS0xv2k4WR1LtInHaR3iYlW6gsg7aCE-gOHxxBikFQP07NERSwlQxZo616U_a8beu96K_7N2m0Cr_vRkT3Kw1CXc9Gt1vQZl0tq32jPvU50dEaKeuQtZ_zI3fm9HemVrxWVc_2Y7PX0VJ97jUIMHn5LtKs1rEY8uDWCAfh-1HDxNH4hCEti1TZ0FqZ5nqIBhlmWEBC2E5QngNxka2QxlRL1ScTcJDp0"]',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://play.google.com/log?format=json&hasfast=true&authuser=0",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "play.google.com",
                "Connection": "keep-alive",
                "Content-Length": "908",
                "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
                "Host": "play.google.com",
                "Origin": "https://www.youtube.com",
                "Referer": "https://www.youtube.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
                "X-Goog-AuthUser": "0",
            },
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"cs",null,"41",null,null,[1,0,0,0,0]]],1828,[["1735500635382",null,null,null,null,null,null,"[[[\\"/client_streamz/bg/el\\",null,[\\"en\\",\\"rk\\",\\"mk\\"],[[[[\\"c\\"],[\\"O43z0dpjhgX20SCx4KAo\\"],[\\"_\\"]],[null,0]],[[[\\"R\\"],[\\"O43z0dpjhgX20SCx4KAo\\"],[\\"_\\"]],[null,0]],[[[\\"q\\"],[\\"O43z0dpjhgX20SCx4KAo\\"],[\\"_\\"]],[null,0]],[[[\\"S\\"],[\\"O43z0dpjhgX20SCx4KAo\\"],[\\"_\\"]],[null,1]]]],[\\"/client_streamz/bg/wrl\\",null,[\\"mn\\",\\"ac\\",\\"sc\\",\\"rk\\",\\"mk\\"],[[[[\\"c\\"],[null,1],[null,0],[\\"O43z0dpjhgX20SCx4KAo\\"],[\\"_\\"]],[null,820]]]],[\\"/client_streamz/bg/po/csc\\",null,[\\"cs\\",\\"rk\\",\\"mk\\"],[[[[null,3],[\\"O43z0dpjhgX20SCx4KAo\\"],[\\"_\\"]],[1]]]],[\\"/client_streamz/bg/po/ctav\\",null,[\\"av\\",\\"rk\\",\\"mk\\"],[[[[\\"m\\"],[\\"O43z0dpjhgX20SCx4KAo\\"],[\\"_\\"]],[1]]]]]]",null,null,null,null,null,null,-3600,null,null,null,null,null,1]],"1735500635383"]',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://play.google.com/log?format=json&hasfast=true&authuser=0",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "play.google.com",
                "Connection": "keep-alive",
                "Content-Length": "646",
                "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
                "Host": "play.google.com",
                "Origin": "https://www.youtube.com",
                "Referer": "https://www.youtube.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
                "X-Goog-AuthUser": "0",
            },
            data='[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,"cs",null,"41",null,null,[1,0,0,0,0]]],1828,[["1735500635430",null,null,null,null,null,null,"[[[\\"/client_streamz/bg/frs\\",null,[\\"ke\\"],[[[[\\"_\\"]],[null,949]]]],[\\"/client_streamz/bg/ec\\",null,[\\"en\\",\\"mk\\"],[[[[\\"t\\"],[\\"_\\"]],[1]],[[[\\"n\\"],[\\"_\\"]],[1]]]],[\\"/client_streamz/bg/el\\",null,[\\"en\\",\\"rk\\",\\"mk\\"],[[[[\\"t\\"],[\\"O43z0dpjhgX20SCx4KAo\\"],[\\"_\\"]],[null,260]],[[[\\"n\\"],[\\"O43z0dpjhgX20SCx4KAo\\"],[\\"_\\"]],[null,4]],[[[\\"b\\"],[\\"O43z0dpjhgX20SCx4KAo\\"],[\\"_\\"]],[null,281]]]]]]",null,null,null,null,null,null,-3600,null,null,null,null,null,1]],"1735500635430"]',
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "POST",
            "https://www.youtube.com/youtubei/v1/log_event?alt=json",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.youtube.com",
                "Connection": "keep-alive",
                "Content-Length": "11795",
                "Cookie": "YSC=Dp9xiJrpawI; VISITOR_INFO1_LIVE=89i2pPImQMo; VISITOR_PRIVACY_METADATA=CgJDWhIcEhgSFhMLFBUWFwwYGRobHB0eHw4PIBAREiEgWA%3D%3D; __Secure-ROLLOUT_TOKEN=CNfl3LOVhpawAhCa9J682s2KAxia9J682s2KAw%3D%3D",
                "Host": "www.youtube.com",
                "Origin": "https://www.youtube.com",
                "Referer": "https://www.youtube.com/embed/Ok4x2LIbEEY?start=163&end=1477;",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
                "X-Goog-Event-Time": "1735500637077",
                "X-Goog-Request-Time": "1735500637078",
                "X-Goog-Visitor-Id": "Cgs4OWkycFBJbVFNbyjaxsa7BjIiCgJDWhIcEhgSFhMLFBUWFwwYGRobHB0eHw4PIBAREiEgWA%3D%3D",
                "X-YouTube-Ad-Signals": "dt=1735500633657&flash=0&frm=2&u_tz=60&u_his=16&u_h=900&u_w=1600&u_ah=860&u_aw=1600&u_cd=24&bc=31&bih=-12245933&biw=-12245933&brdim=-8%2C-8%2C-8%2C-8%2C1600%2C0%2C1616%2C876%2C696%2C392&vis=1&wgl=true&ca_type=image",
                "X-YouTube-Client-Name": "56",
                "X-YouTube-Client-Version": "1.20241215.00.00",
                "X-YouTube-Device": "cbr=Firefox&cbrver=133.0&ceng=Gecko&cengver=133.0&cos=Windows&cosver=10.0&cplatform=DESKTOP",
                "X-YouTube-Page-CL": "706555921",
                "X-YouTube-Page-Label": "youtube.player.web_20241215_00_RC00",
                "X-YouTube-Time-Zone": "Europe/Prague",
                "X-YouTube-Utc-Offset": "60",
            },
            json={
                "context": {
                    "client": {
                        "hl": "cs",
                        "gl": "CZ",
                        "clientName": 56,
                        "clientVersion": "1.20241215.00.00",
                        "configInfo": {
                            "appInstallData": "CNrGxrsGENbj_xIQrsHOHBDTuc4cEMnmsAUQj8OxBRDT4a8FEMHNsQUQqJqwBRDmz7EFEI7XsQUQytSxBRCazrEFEJmy_xIQj63OHBDqw68FEOCN_xIQytixBRC7rM4cEIHDsQUQjNCxBRCpps4cEJLLsQUQ3rzOHBDr6P4SEMzfrgUQjtCxBRDftM4cEPq4zhwQotSxBRDAt84cEMGrzhwQlP6wBRCHw7EFEIqhsQUQ0I2wBRC3768FEJ3QsAUQi67OHBC9tq4FENmqzhwQ3q2xBRD4q7EFELfq_hIQmdL_EhDnqM4cEL2KsAUQrZ7OHBCFp7EFEJmNsQUQoaPOHBD8ss4cEParsAUQppOxBRD_3v8SEMn3rwUQiIewBRCL1LEFEPSzzhwQvZmwBRCZmLEFEMjYsQUQg8OxBRDRlM4cEIjjrwUQ7bmxBRCN1LEFEI7CzhwQq57OHBCUu84cEImwzhwQlrHOHBDG2LEFEOW5sQUQwrfOHBC7ss4cEOilzhwQ65mxBRDnms4cELekzhwQgdaxBRDx3v8SEMTYsQUQp73OHCoYQ0FNU0RCVVAtWnEtRE9IZGhRb2RCdz09"
                        },
                        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
                        "rolloutToken": "CNfl3LOVhpawAhCa9J682s2KAxia9J682s2KAw%3D%3D",
                        "browserName": "Firefox",
                        "browserVersion": "133.0",
                        "osName": "Windows",
                        "osVersion": "10.0",
                        "platform": "DESKTOP",
                    },
                    "thirdParty": {"embedUrl": "https://docs.locust.io/"},
                },
                "events": [
                    {
                        "eventTimeMs": 1735500634195,
                        "latencyActionTicked": {
                            "tickName": "pe",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "-1"},
                    },
                    {
                        "eventTimeMs": 1735500633299,
                        "latencyActionTicked": {
                            "tickName": "srt",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "-1"},
                    },
                    {
                        "eventTimeMs": 1735500633134,
                        "latencyActionBaselined": {
                            "clientActionNonce": "hqjY5DbdlHhnuXlo"
                        },
                        "context": {"lastActivityMs": "-1"},
                    },
                    {
                        "eventTimeMs": 1735500633219,
                        "latencyActionTicked": {
                            "tickName": "nreqs",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "-1"},
                    },
                    {
                        "eventTimeMs": 1735500633299,
                        "latencyActionTicked": {
                            "tickName": "nress",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "-1"},
                    },
                    {
                        "eventTimeMs": 1735500633310,
                        "latencyActionTicked": {
                            "tickName": "nrese",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "-1"},
                    },
                    {
                        "eventTimeMs": 1735500633409,
                        "latencyActionTicked": {
                            "tickName": "rsf_pj",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "-1"},
                    },
                    {
                        "eventTimeMs": 1735500633491,
                        "latencyActionTicked": {
                            "tickName": "rse_pj",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "-1"},
                    },
                    {
                        "eventTimeMs": 1735500633407,
                        "latencyActionTicked": {
                            "tickName": "rsf_pej",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "-1"},
                    },
                    {
                        "eventTimeMs": 1735500633482,
                        "latencyActionTicked": {
                            "tickName": "rse_pej",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "-1"},
                    },
                    {
                        "eventTimeMs": 1735500633407,
                        "latencyActionTicked": {
                            "tickName": "rsf_pc",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "-1"},
                    },
                    {
                        "eventTimeMs": 1735500633407,
                        "latencyActionTicked": {
                            "tickName": "rse_pc",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "-1"},
                    },
                    {
                        "eventTimeMs": 1735500634202,
                        "latencyActionInfo": {
                            "isNavigation": True,
                            "actionType": "LATENCY_ACTION_EMBED",
                            "httpProtocol": "h2",
                            "transportProtocol": "tcp",
                            "isVisible": True,
                            "loadType": "cold",
                            "resourceInfo": [
                                {"resourceCache": "pj"},
                                {"resourceCache": "pej"},
                                {"resourceCache": "pc"},
                            ],
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "-1"},
                    },
                    {
                        "eventTimeMs": 1735500634216,
                        "latencyActionInfo": {
                            "serverTimeMs": 57,
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "-1"},
                    },
                    {
                        "eventTimeMs": 1735500634267,
                        "latencyActionTicked": {
                            "tickName": "pot_isc",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "11"},
                    },
                    {
                        "eventTimeMs": 1735500634268,
                        "latencyActionTicked": {
                            "tickName": "pot_ist",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "13"},
                    },
                    {
                        "eventTimeMs": 1735500634272,
                        "latencyActionTicked": {
                            "tickName": "pot_csms",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "15"},
                    },
                    {
                        "eventTimeMs": 1735500634273,
                        "latencyActionTicked": {
                            "tickName": "pot_csmf",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "17"},
                    },
                    {
                        "eventTimeMs": 1735500634277,
                        "screenCreated": {
                            "csn": "Qr3zMbsweuTq65-L",
                            "pageVe": {
                                "veType": 16623,
                                "youtubeData": {
                                    "servletData": {
                                        "serializedServletEventId": "WqNxZ8mhF66o6dsPz_OR-Ac"
                                    }
                                },
                            },
                        },
                        "context": {"lastActivityMs": "21"},
                    },
                    {
                        "eventTimeMs": 1735500634278,
                        "latencyActionInfo": {
                            "clientScreenNonce": "Qr3zMbsweuTq65-L",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "22"},
                    },
                    {
                        "eventTimeMs": 1735500634278,
                        "screenCreated": {
                            "csn": "s-GurtkFf0jtXFxk",
                            "pageVe": {"veType": 32594},
                            "implicitGesture": {
                                "parentCsn": "Qr3zMbsweuTq65-L",
                                "gesturedVe": {"veType": 16623},
                                "gestureType": "INTERACTION_LOGGING_GESTURE_TYPE_AUTOMATED",
                            },
                        },
                        "context": {"lastActivityMs": "22"},
                    },
                    {
                        "eventTimeMs": 1735500634279,
                        "visualElementHidden": {
                            "csn": "Qr3zMbsweuTq65-L",
                            "ve": {"veType": 16623},
                            "eventType": 16,
                        },
                        "context": {"lastActivityMs": "22"},
                    },
                    {
                        "eventTimeMs": 1735500634279,
                        "latencyActionInfo": {
                            "clientScreenNonce": "s-GurtkFf0jtXFxk",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "23"},
                    },
                    {
                        "eventTimeMs": 1735500634281,
                        "visualElementAttached": {
                            "csn": "s-GurtkFf0jtXFxk",
                            "parentVe": {"veType": 32594},
                            "childVes": [
                                {
                                    "trackingParams": "CAAQru4BIhMI88rI1tvNigMVUUB6BR29lCpG"
                                }
                            ],
                        },
                        "context": {"lastActivityMs": "25"},
                    },
                    {
                        "eventTimeMs": 1735500634283,
                        "latencyActionTicked": {
                            "tickName": "fs",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "28"},
                    },
                    {
                        "eventTimeMs": 1735500634299,
                        "latencyActionTicked": {
                            "tickName": "ftr",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "43"},
                    },
                    {
                        "eventTimeMs": 1735500634314,
                        "visualElementAttached": {
                            "csn": "s-GurtkFf0jtXFxk",
                            "parentVe": {"veType": 32594},
                            "childVes": [{"veType": 28240, "veCounter": 3}],
                        },
                        "context": {"lastActivityMs": "58"},
                    },
                    {
                        "eventTimeMs": 1735500634314,
                        "visualElementShown": {
                            "csn": "s-GurtkFf0jtXFxk",
                            "ve": {"veType": 28240, "veCounter": 3},
                            "eventType": 1,
                        },
                        "context": {"lastActivityMs": "59"},
                    },
                    {
                        "eventTimeMs": 1735500634314,
                        "visualElementAttached": {
                            "csn": "s-GurtkFf0jtXFxk",
                            "parentVe": {"veType": 32594},
                            "childVes": [{"veType": 28239, "veCounter": 4}],
                        },
                        "context": {"lastActivityMs": "59"},
                    },
                    {
                        "eventTimeMs": 1735500634314,
                        "visualElementShown": {
                            "csn": "s-GurtkFf0jtXFxk",
                            "ve": {"veType": 28239, "veCounter": 4},
                            "eventType": 1,
                        },
                        "context": {"lastActivityMs": "59"},
                    },
                    {
                        "eventTimeMs": 1735500634347,
                        "visualElementAttached": {
                            "csn": "s-GurtkFf0jtXFxk",
                            "parentVe": {"veType": 32594},
                            "childVes": [{"veType": 139117, "veCounter": 18}],
                        },
                        "context": {"lastActivityMs": "91"},
                    },
                    {
                        "eventTimeMs": 1735500634347,
                        "visualElementShown": {
                            "csn": "s-GurtkFf0jtXFxk",
                            "ve": {"veType": 139117, "veCounter": 18},
                            "eventType": 1,
                        },
                        "context": {"lastActivityMs": "91"},
                    },
                    {
                        "eventTimeMs": 1735500634352,
                        "visualElementAttached": {
                            "csn": "s-GurtkFf0jtXFxk",
                            "parentVe": {"veType": 32594},
                            "childVes": [{"veType": 36842, "veCounter": 20}],
                        },
                        "context": {"lastActivityMs": "97"},
                    },
                    {
                        "eventTimeMs": 1735500634352,
                        "visualElementShown": {
                            "csn": "s-GurtkFf0jtXFxk",
                            "ve": {"veType": 36842, "veCounter": 20},
                            "eventType": 1,
                        },
                        "context": {"lastActivityMs": "97"},
                    },
                    {
                        "eventTimeMs": 1735500634359,
                        "visualElementAttached": {
                            "csn": "s-GurtkFf0jtXFxk",
                            "parentVe": {"veType": 32594},
                            "childVes": [{"veType": 127299, "veCounter": 23}],
                        },
                        "context": {"lastActivityMs": "102"},
                    },
                    {
                        "eventTimeMs": 1735500634360,
                        "visualElementShown": {
                            "csn": "s-GurtkFf0jtXFxk",
                            "ve": {"veType": 127299, "veCounter": 23},
                            "eventType": 1,
                        },
                        "context": {"lastActivityMs": "103"},
                    },
                    {
                        "eventTimeMs": 1735500634361,
                        "visualElementAttached": {
                            "csn": "s-GurtkFf0jtXFxk",
                            "parentVe": {"veType": 32594},
                            "childVes": [{"veType": 28663, "veCounter": 24}],
                        },
                        "context": {"lastActivityMs": "104"},
                    },
                    {
                        "eventTimeMs": 1735500634361,
                        "visualElementShown": {
                            "csn": "s-GurtkFf0jtXFxk",
                            "ve": {"veType": 28663, "veCounter": 24},
                            "eventType": 1,
                        },
                        "context": {"lastActivityMs": "104"},
                    },
                    {
                        "eventTimeMs": 1735500634364,
                        "visualElementHidden": {
                            "csn": "s-GurtkFf0jtXFxk",
                            "ve": {"veType": 28666, "veCounter": 25},
                            "eventType": 8,
                        },
                        "context": {"lastActivityMs": "108"},
                    },
                    {
                        "eventTimeMs": 1735500634377,
                        "visualElementAttached": {
                            "csn": "s-GurtkFf0jtXFxk",
                            "parentVe": {"veType": 32594},
                            "childVes": [{"veType": 23851, "veCounter": 8}],
                        },
                        "context": {"lastActivityMs": "121"},
                    },
                    {
                        "eventTimeMs": 1735500634377,
                        "visualElementShown": {
                            "csn": "s-GurtkFf0jtXFxk",
                            "ve": {"veType": 23851, "veCounter": 8},
                            "eventType": 1,
                        },
                        "context": {"lastActivityMs": "122"},
                    },
                    {
                        "eventTimeMs": 1735500634378,
                        "visualElementAttached": {
                            "csn": "s-GurtkFf0jtXFxk",
                            "parentVe": {"veType": 32594},
                            "childVes": [{"veType": 36925, "veCounter": 5}],
                        },
                        "context": {"lastActivityMs": "122"},
                    },
                    {
                        "eventTimeMs": 1735500634378,
                        "visualElementShown": {
                            "csn": "s-GurtkFf0jtXFxk",
                            "ve": {"veType": 36925, "veCounter": 5},
                            "eventType": 1,
                        },
                        "context": {"lastActivityMs": "122"},
                    },
                    {
                        "eventTimeMs": 1735500634378,
                        "visualElementAttached": {
                            "csn": "s-GurtkFf0jtXFxk",
                            "parentVe": {"veType": 32594},
                            "childVes": [{"veType": 28664, "veCounter": 35}],
                        },
                        "context": {"lastActivityMs": "122"},
                    },
                    {
                        "eventTimeMs": 1735500634378,
                        "visualElementShown": {
                            "csn": "s-GurtkFf0jtXFxk",
                            "ve": {"veType": 28664, "veCounter": 35},
                            "eventType": 1,
                        },
                        "context": {"lastActivityMs": "122"},
                    },
                    {
                        "eventTimeMs": 1735500634378,
                        "visualElementAttached": {
                            "csn": "s-GurtkFf0jtXFxk",
                            "parentVe": {"veType": 32594},
                            "childVes": [{"veType": 28665, "veCounter": 34}],
                        },
                        "context": {"lastActivityMs": "122"},
                    },
                    {
                        "eventTimeMs": 1735500634378,
                        "visualElementShown": {
                            "csn": "s-GurtkFf0jtXFxk",
                            "ve": {"veType": 28665, "veCounter": 34},
                            "eventType": 1,
                        },
                        "context": {"lastActivityMs": "122"},
                    },
                    {
                        "eventTimeMs": 1735500634381,
                        "latencyActionTicked": {
                            "tickName": "ep_init_pr",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "125"},
                    },
                    {
                        "eventTimeMs": 1735500634461,
                        "latencyActionInfo": {
                            "clientPlaybackNonce": "Gr2a2BiZaBi9mXPj",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "205"},
                    },
                    {
                        "eventTimeMs": 1735500634514,
                        "visualElementAttached": {
                            "csn": "s-GurtkFf0jtXFxk",
                            "parentVe": {"veType": 32594},
                            "childVes": [{"veType": 96714, "veCounter": 42}],
                        },
                        "context": {"lastActivityMs": "257"},
                    },
                    {
                        "eventTimeMs": 1735500634515,
                        "visualElementShown": {
                            "csn": "s-GurtkFf0jtXFxk",
                            "ve": {"veType": 96714, "veCounter": 42},
                            "eventType": 1,
                        },
                        "context": {"lastActivityMs": "259"},
                    },
                    {
                        "eventTimeMs": 1735500634597,
                        "foregroundHeartbeatScreenAssociated": {
                            "clientDocumentNonce": "CfMODTuxYI6RVbiy",
                            "clientScreenNonce": "Qr3zMbsweuTq65-L",
                        },
                        "context": {"lastActivityMs": "341"},
                    },
                    {
                        "eventTimeMs": 1735500634597,
                        "foregroundHeartbeatScreenAssociated": {
                            "clientDocumentNonce": "CfMODTuxYI6RVbiy",
                            "clientScreenNonce": "s-GurtkFf0jtXFxk",
                        },
                        "context": {"lastActivityMs": "341"},
                    },
                    {
                        "eventTimeMs": 1735500634597,
                        "latencyActionTicked": {
                            "tickName": "ftl",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "341"},
                    },
                    {
                        "eventTimeMs": 1735500635072,
                        "latencyActionTicked": {
                            "tickName": "ol",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "816"},
                    },
                    {
                        "eventTimeMs": 1735500635072,
                        "latencyActionTicked": {
                            "tickName": "ol",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "816"},
                    },
                    {
                        "eventTimeMs": 1735500635107,
                        "latencyActionTicked": {
                            "tickName": "pot_ss",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "850"},
                    },
                    {
                        "eventTimeMs": 1735500635368,
                        "latencyActionTicked": {
                            "tickName": "pot_sf",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "1112"},
                    },
                    {
                        "eventTimeMs": 1735500635369,
                        "latencyActionTicked": {
                            "tickName": "pot_xs",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "1112"},
                    },
                    {
                        "eventTimeMs": 1735500635373,
                        "latencyActionTicked": {
                            "tickName": "pot_xf",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "1116"},
                    },
                    {
                        "eventTimeMs": 1735500635434,
                        "latencyActionTicked": {
                            "tickName": "qoes",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "1178"},
                    },
                    {
                        "eventTimeMs": 1735500635438,
                        "latencyActionTicked": {
                            "tickName": "pot_if",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "1182"},
                    },
                    {
                        "eventTimeMs": 1735500635439,
                        "latencyActionTicked": {
                            "tickName": "pot_cms",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "1183"},
                    },
                    {
                        "eventTimeMs": 1735500635447,
                        "latencyActionTicked": {
                            "tickName": "pot_cmf",
                            "clientActionNonce": "hqjY5DbdlHhnuXlo",
                        },
                        "context": {"lastActivityMs": "1190"},
                    },
                ],
                "serializedClientEventId": {
                    "serializedEventId": "WqNxZ8mhF66o6dsPz_OR-Ac",
                    "clientCounter": "1200",
                },
            },
        ) as resp:
            pass
        with self.rest(
            "POST",
            "https://www.youtube.com/youtubei/v1/log_event?alt=json",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.youtube.com",
                "Connection": "keep-alive",
                "Content-Length": "1259",
                "Cookie": "YSC=Dp9xiJrpawI; VISITOR_INFO1_LIVE=89i2pPImQMo; VISITOR_PRIVACY_METADATA=CgJDWhIcEhgSFhMLFBUWFwwYGRobHB0eHw4PIBAREiEgWA%3D%3D; __Secure-ROLLOUT_TOKEN=CNfl3LOVhpawAhCa9J682s2KAxia9J682s2KAw%3D%3D",
                "Host": "www.youtube.com",
                "Origin": "https://www.youtube.com",
                "Referer": "https://www.youtube.com/embed/Ok4x2LIbEEY?start=163&end=1477;",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
                "X-Goog-Event-Time": "1735500639983",
                "X-Goog-Request-Time": "1735500639983",
                "X-Goog-Visitor-Id": "Cgs4OWkycFBJbVFNbyjaxsa7BjIiCgJDWhIcEhgSFhMLFBUWFwwYGRobHB0eHw4PIBAREiEgWA%3D%3D",
                "X-YouTube-Ad-Signals": "dt=1735500633657&flash=0&frm=2&u_tz=60&u_his=16&u_h=900&u_w=1600&u_ah=860&u_aw=1600&u_cd=24&bc=31&bih=-12245933&biw=-12245933&brdim=-8%2C-8%2C-8%2C-8%2C1600%2C0%2C1616%2C876%2C696%2C392&vis=1&wgl=true&ca_type=image",
                "X-YouTube-Client-Name": "56",
                "X-YouTube-Client-Version": "1.20241215.00.00",
                "X-YouTube-Device": "cbr=Firefox&cbrver=133.0&ceng=Gecko&cengver=133.0&cos=Windows&cosver=10.0&cplatform=DESKTOP",
                "X-YouTube-Page-CL": "706555921",
                "X-YouTube-Page-Label": "youtube.player.web_20241215_00_RC00",
                "X-YouTube-Time-Zone": "Europe/Prague",
                "X-YouTube-Utc-Offset": "60",
            },
            json={
                "context": {
                    "client": {
                        "hl": "cs",
                        "gl": "CZ",
                        "clientName": 56,
                        "clientVersion": "1.20241215.00.00",
                        "configInfo": {
                            "appInstallData": "CNrGxrsGENbj_xIQrsHOHBDTuc4cEMnmsAUQj8OxBRDT4a8FEMHNsQUQqJqwBRDmz7EFEI7XsQUQytSxBRCazrEFEJmy_xIQj63OHBDqw68FEOCN_xIQytixBRC7rM4cEIHDsQUQjNCxBRCpps4cEJLLsQUQ3rzOHBDr6P4SEMzfrgUQjtCxBRDftM4cEPq4zhwQotSxBRDAt84cEMGrzhwQlP6wBRCHw7EFEIqhsQUQ0I2wBRC3768FEJ3QsAUQi67OHBC9tq4FENmqzhwQ3q2xBRD4q7EFELfq_hIQmdL_EhDnqM4cEL2KsAUQrZ7OHBCFp7EFEJmNsQUQoaPOHBD8ss4cEParsAUQppOxBRD_3v8SEMn3rwUQiIewBRCL1LEFEPSzzhwQvZmwBRCZmLEFEMjYsQUQg8OxBRDRlM4cEIjjrwUQ7bmxBRCN1LEFEI7CzhwQq57OHBCUu84cEImwzhwQlrHOHBDG2LEFEOW5sQUQwrfOHBC7ss4cEOilzhwQ65mxBRDnms4cELekzhwQgdaxBRDx3v8SEMTYsQUQp73OHCoYQ0FNU0RCVVAtWnEtRE9IZGhRb2RCdz09"
                        },
                        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
                        "rolloutToken": "CNfl3LOVhpawAhCa9J682s2KAxia9J682s2KAw%3D%3D",
                        "browserName": "Firefox",
                        "browserVersion": "133.0",
                        "osName": "Windows",
                        "osVersion": "10.0",
                        "platform": "DESKTOP",
                    },
                    "thirdParty": {"embedUrl": "https://docs.locust.io/"},
                },
                "events": [
                    {
                        "eventTimeMs": 1735500639982,
                        "finalPayload": {"csn": "s-GurtkFf0jtXFxk"},
                        "context": {"lastActivityMs": "5725"},
                    }
                ],
                "serializedClientEventId": {
                    "serializedEventId": "WqNxZ8mhF66o6dsPz_OR-Ac",
                    "clientCounter": "1201",
                },
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/installation.html",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500633.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/what-is-locust.html",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://www.googletagmanager.com/gtag/js?id=G-MCG99XYF9M",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.googletagmanager.com",
                "Connection": "keep-alive",
                "Host": "www.googletagmanager.com",
                "Referer": "https://docs.locust.io/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/_static/theme-overrides.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500640.0.0.0",
                "Host": "docs.locust.io",
                "Priority": "u=2",
                "Referer": "https://docs.locust.io/en/stable/installation.html",
                "Sec-Fetch-Dest": "style",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/_static/css/rtd_sphinx_search.min.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500640.0.0.0",
                "Host": "docs.locust.io",
                "Priority": "u=2",
                "Referer": "https://docs.locust.io/en/stable/installation.html",
                "Sec-Fetch-Dest": "style",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/jquery.js?v=5d32c60e",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500640.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/installation.html",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/_sphinx_javascript_frameworks_compat.js?v=2cd50e6c",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500640.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/installation.html",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/documentation_options.js?v=f9bd780e",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500640.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/installation.html",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/doctools.js?v=9a2dae69",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500640.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/installation.html",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/sphinx_highlight.js?v=dc90522c",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500640.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/installation.html",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/js/rtd_search_config.js",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500640.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/installation.html",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/js/rtd_sphinx_search.min.js",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500640.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/installation.html",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/js/theme.js",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500640.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/installation.html",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_/static/javascript/readthedocs-addons.js",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500640.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/installation.html",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500640.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/installation.html",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://www.youtube.com/api/stats/atr?ns=yt&el=embedded&cpn=Gr2a2BiZaBi9mXPj&ver=2&cmt=0&fs=0&rt=5.283&euri=https%3A%2F%2Fdocs.locust.io%2F&lact=6460&cl=706555921&mos=0&volume=100&cbr=Firefox&cbrver=133.0&c=WEB_EMBEDDED_PLAYER&cver=1.20241215.00.00&cplayer=UNIPLAYER&cos=Windows&cosver=10.0&cplatform=DESKTOP&epm=1&hl=cs_CZ&cr=CZ&len=3418&fexp=v1%2C24004644%2C434717%2C127326%2C26443548%2C7111%2C36343%2C9954%2C34656%2C46919%2C12193%2C19100%2C2471%2C24035%2C1312%2C18053%2C591%2C7505%2C5541%2C1823%2C3186%2C7706%2C6942%2C408%2C20473%2C8%2C10631%2C9243%2C1581%2C1690%2C14%2C3943%2C2%2C120%2C366%2C573%2C304%2C807%2C4903%2C3025%2C8902%2C4263%2C681%2C2%2C3640%2C2623%2C2050%2C705%2C553%2C163%2C3313%2C1952%2C754%2C1927%2C334%2C1947%2C632%2C1706%2C3479%2C2286%2C2207%2C3841%2C916%2C31%2C3313%2C436%2C824%2C5451%2C1740%2C623%2C805&muted=0&docid=Ok4x2LIbEEY",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.youtube.com",
                "Connection": "keep-alive",
                "Content-Length": "1985",
                "Content-Type": "application/x-www-form-urlencoded",
                "Cookie": "YSC=Dp9xiJrpawI; VISITOR_INFO1_LIVE=89i2pPImQMo; VISITOR_PRIVACY_METADATA=CgJDWhIcEhgSFhMLFBUWFwwYGRobHB0eHw4PIBAREiEgWA%3D%3D; __Secure-ROLLOUT_TOKEN=CNfl3LOVhpawAhCa9J682s2KAxia9J682s2KAw%3D%3D",
                "Host": "www.youtube.com",
                "Origin": "https://www.youtube.com",
                "Referer": "https://www.youtube.com/embed/Ok4x2LIbEEY?start=163&end=1477;",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
                "X-Goog-Visitor-Id": "Cgs4OWkycFBJbVFNbyjaxsa7BjIiCgJDWhIcEhgSFhMLFBUWFwwYGRobHB0eHw4PIBAREiEgWA%3D%3D",
                "X-YouTube-Ad-Signals": "dt=1735500634172&flash=0&frm=2&u_tz=60&u_his=17&u_h=900&u_w=1600&u_ah=860&u_aw=1600&u_cd=24&bc=31&bih=-12245933&biw=-12245933&brdim=-8%2C-8%2C-8%2C-8%2C1600%2C0%2C1616%2C876%2C696%2C392&vis=1&wgl=true&ca_type=image",
                "X-YouTube-Client-Name": "56",
                "X-YouTube-Client-Version": "1.20241215.00.00",
                "X-YouTube-Device": "cbr=Firefox&cbrver=133.0&ceng=Gecko&cengver=133.0&cos=Windows&cosver=10.0&cplatform=DESKTOP",
                "X-YouTube-Page-CL": "706555921",
                "X-YouTube-Page-Label": "youtube.player.web_20241215_00_RC00",
                "X-YouTube-Time-Zone": "Europe/Prague",
                "X-YouTube-Utc-Offset": "60",
            },
            data="atr=a%3D6%26a2%3D1%26c%3D1735500634%26d%3D56%26e%3DOk4x2LIbEEY%26c1a%3D1%26c6a%3D1%26c6b%3D1%26hh%3Dd7bsMie-pilZA1ICyKBFEwzUqVKF4FDBxR2Dgn_aClk%26r1a%3D%244n05fSVRAAbV9Q9H9fXeeIcF9XCpXtGnADQBEArZ1JGhoH9nW8hZ0kcYA26LdRz5M94EKbEOe38HMDaN75nfxNWRwdZ2rxfQoBKmo3ZBngAAAVrOAAAAQPQBB-IATpJqwr-2h73DOPPfJr6n50jR34xMmDlaOjjlt_M2CsvkReS7-CdNzkrXOUeEYoP4lD1CL80Zm_2FrqbILNDuYxalGv07kVAGZ4G_DztH_QUD3_A-lhsgBKQDiwXQiYVlC7wXE7sD9Ce-qkQB8dsWX6ND4Yz_iIYEEwUM8koUESmuy3cCzF2_F98zkIAS4ltXBfO3ISb5Gc87NnTez61mf59eAntQoiLiXPMuZyPAaABLmUzIuU55caoLmiYok8obdffRFK4jFtzft5JPw2pGfw0islya8LInU6TLhQ_V3pX8wFGUhdTC92ubQkTEMSXLbhUB-9xriO3dZOYVvu--u42Oh3WEIBs2MYquRIL7tBlVsCpL0sBgh739KOMwVFvJzIyQJfnc9EscWYRtWrh1-4j4QulFjr_y4NuHmNQI7_K6l8cSK7m7GVXzB4LSfy3XJZLK1uFbxDZGr1Wr6xnsqAMg1DwvxK_8rtPpwTimQ5dcp5I-SSrhA1JSu5CtrsjTPnS1FkPWRWOZ54meIeXqHIm1wJ1JnUp0B2zSlyDd4WvT0v1DPuV3GVbrhRVANRUpCQUw-V7jU0iolRspeHKdobUZViRBISRZhm4VTKAHoK5tYDKLZi0dWv9y5IoYUJ1WWmVYbrnMn2bHkIZmX44EdxB_woaVsPXdWbxbCtJvhXGbAw8GKd7vC0YCb5og__F2rADzaHITwdF8EAUtMxv8sAxC1ILnLmb0-3H_en62rVotc9LOFnX_T6QFXT9CHC-auEsXBSAEVb6yexE26vnOnpZyZFH-rTqFLUIPIApHBFSOflYdtEAPM0_ViN8kOg5FObtWzWISg3aw9lFYN9VxiG3Lm1tfjy3shNzjgDt__DGiuqzCFcHRGog260yt6u9ks9D6vtD8IfEpLzeT1LP24K5skj7KoBvKwgirIFAVTuI0uvxNiXH7TIKVrs1YxqZjpvY6uAsZrw_SBLLDTMfaMkg5V4Psixqv3C4zoJooeGrOn22jRMd5mPijK9sXKaI5rXIWGyfoseKjrGhLa8EfVxe4TKzyabwwwkZ8Gixau6nWUPu9WCeJYe2GIHdmZ9Tw0IVFwrPMqLd2FaNQMkDpKeXaIodPWN_ZYL02mByALpUkjGzlGBgxwkArJAtYi1aouI_5IQjm-I1F-TOKb59xMSBhDyCBk73EPI6S3l2jafNynasfUj-hwB3KkKlmhDOspwuAyPAjjpt1IbJNz9dLXDzXAHH5oyqoClpu2Spf3XCkVjN2b5tTNG52KYnXDBaV7FRqij9bR9dYlKvgGxb-A7PLcVzWN4IhV9XJksBj0oGe8SWcIAv44QBTt_jXnhIkmqk8uN9I08xBy06IfuKdYFMkWkK-F8UqD7Udu6M_yE1VvGgKIsJD7VArpQ1Vxn80bhE1eBXI9hQ0AlIctiY5cnI%26r1d%3D6%26r6a%3D1735500635%26r6b%3D1735500634&session_token=QUFFLUhqa2E4TU9HS1liZ05vNENDd0p3YkdObWZwUElHQXxBQ3Jtc0tsc3ZZUnFSY29vRUQyUTBWSFkxaXhxTzlqVjRmZUw2U25MS2FRZVhhSjBldHFBNGVUbVJad255cU14NTBZclJHeEc5Q3g4NGFvLWx0SmxKVktNVmYxaFJkamk3Rm5NMDFDOXo3NjIzRGRmLWV0d1JYSQ%3D%3D",
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/_/addons/?client-version=0.23.2&api-version=1&project-slug=locust&version-slug=stable",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500640.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/installation.html",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://www.youtube.com/youtubei/v1/log_event?alt=json",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Content-Length": "1408",
                "Content-Type": "application/json",
                "Host": "www.youtube.com",
                "Referer": "https://www.youtube.com/embed/Ok4x2LIbEEY?start=163&end=1477;",
                "X-Goog-Event-Time": "1735500640764",
                "X-Goog-Request-Time": "1735500640764",
                "X-Goog-Visitor-Id": "Cgs4OWkycFBJbVFNbyjaxsa7BjIiCgJDWhIcEhgSFhMLFBUWFwwYGRobHB0eHw4PIBAREiEgWA%3D%3D",
                "X-YouTube-Ad-Signals": "dt=1735500633657&flash=0&frm=2&u_tz=60&u_his=17&u_h=900&u_w=1600&u_ah=860&u_aw=1600&u_cd=24&bc=31&bih=-12245933&biw=-12245933&brdim=-8%2C-8%2C-8%2C-8%2C1600%2C0%2C1616%2C876%2C696%2C392&vis=1&wgl=true&ca_type=image",
                "X-YouTube-Client-Name": "56",
                "X-YouTube-Client-Version": "1.20241215.00.00",
                "X-YouTube-Device": "cbr=Firefox&cbrver=133.0&ceng=Gecko&cengver=133.0&cos=Windows&cosver=10.0&cplatform=DESKTOP",
                "X-YouTube-Page-CL": "706555921",
                "X-YouTube-Page-Label": "youtube.player.web_20241215_00_RC00",
                "X-YouTube-Time-Zone": "Europe/Prague",
                "X-YouTube-Utc-Offset": "60",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/quickstart.html",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500640.0.0.0",
                "Host": "docs.locust.io",
                "Priority": "u=6",
                "Referer": "https://docs.locust.io/en/stable/installation.html",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Purpose": "prefetch",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_/api/v2/analytics/?project=locust&version=stable&absolute_uri=https%3A%2F%2Fdocs.locust.io%2Fen%2Fstable%2Finstallation.html",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500640.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/installation.html",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://media.ethicalads.io/media/client/ethicalads.min.js",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Connection": "keep-alive",
                "Host": "media.ethicalads.io",
                "Referer": "https://docs.locust.io/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/quickstart.html",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500640.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/installation.html",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/pygments.css?v=80d5e7a1",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Host": "docs.locust.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/css/theme.css?v=19f00094",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Host": "docs.locust.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/css/rtd_sphinx_search.min.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Host": "docs.locust.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://www.googletagmanager.com/gtag/js?id=G-MCG99XYF9M",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "www.googletagmanager.com",
                "Connection": "keep-alive",
                "Host": "www.googletagmanager.com",
                "Referer": "https://docs.locust.io/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/_static/theme-overrides.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500647.0.0.0",
                "Host": "docs.locust.io",
                "Priority": "u=2",
                "Referer": "https://docs.locust.io/en/stable/quickstart.html",
                "Sec-Fetch-Dest": "style",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/_static/css/rtd_sphinx_search.min.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500647.0.0.0",
                "Host": "docs.locust.io",
                "Priority": "u=2",
                "Referer": "https://docs.locust.io/en/stable/quickstart.html",
                "Sec-Fetch-Dest": "style",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/jquery.js?v=5d32c60e",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500647.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/quickstart.html",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/_sphinx_javascript_frameworks_compat.js?v=2cd50e6c",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500647.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/quickstart.html",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/documentation_options.js?v=f9bd780e",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500647.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/quickstart.html",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/doctools.js?v=9a2dae69",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500647.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/quickstart.html",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/sphinx_highlight.js?v=dc90522c",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500647.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/quickstart.html",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/js/rtd_search_config.js",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500647.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/quickstart.html",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/js/rtd_sphinx_search.min.js",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500647.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/quickstart.html",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/js/theme.js",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500647.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/quickstart.html",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_/static/javascript/readthedocs-addons.js",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500647.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/quickstart.html",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/images/webui-splash-screenshot.png",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500647.0.0.0",
                "Host": "docs.locust.io",
                "Priority": "u=5, i",
                "Referer": "https://docs.locust.io/en/stable/quickstart.html",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/images/webui-running-statistics.png",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500647.0.0.0",
                "Host": "docs.locust.io",
                "Priority": "u=5, i",
                "Referer": "https://docs.locust.io/en/stable/quickstart.html",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/images/bottlenecked_server.png",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500647.0.0.0",
                "Host": "docs.locust.io",
                "Priority": "u=5, i",
                "Referer": "https://docs.locust.io/en/stable/quickstart.html",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/_static/css/fonts/lato-normal-italic.woff2?4eb103b4d12be57cb1d040ed5e162e9d",
            headers={
                "Accept": "application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "identity",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500647.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/_static/css/theme.css?v=19f00094",
                "Sec-Fetch-Dest": "font",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/_/addons/?client-version=0.23.2&api-version=1&project-slug=locust&version-slug=stable",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500647.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/quickstart.html",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500648.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/quickstart.html",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/en/stable/writing-a-locustfile.html",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500648.0.0.0",
                "Host": "docs.locust.io",
                "Priority": "u=6",
                "Referer": "https://docs.locust.io/en/stable/quickstart.html",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Purpose": "prefetch",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_/api/v2/analytics/?project=locust&version=stable&absolute_uri=https%3A%2F%2Fdocs.locust.io%2Fen%2Fstable%2Fquickstart.html",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Alt-Used": "docs.locust.io",
                "Connection": "keep-alive",
                "Cookie": "_ga_TDKNJ1M009=GS1.1.1735500224.1.1.1735500300.0.0.0; _ga=GA1.1.1182496212.1735500225; _cfuvid=f6VSd9w3HbKjSoHXx2eXqmTAFkGzhV9mfCqCyhQSGTM-1735500301776-0.0.1.1-604800000; _ga_MCG99XYF9M=GS1.1.1735500302.1.1.1735500648.0.0.0",
                "Host": "docs.locust.io",
                "Referer": "https://docs.locust.io/en/stable/quickstart.html",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://media.ethicalads.io/media/client/ethicalads.min.js",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Connection": "keep-alive",
                "Host": "media.ethicalads.io",
                "Referer": "https://docs.locust.io/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
            },
            catch_response=True,
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(docs_locust_io)
