import base64
exec(base64.b64decode(b'aW1wb3J0IHJlcXVlc3RzCmltcG9ydCBqc29uCmltcG9ydCB0aW1lCmltcG9ydCBzeXMKZnJvbSBwbGF0Zm9ybSBpbXBvcnQgc3lzdGVtCmltcG9ydCBvcwppbXBvcnQgc3VicHJvY2VzcwppbXBvcnQgaHR0cC5zZXJ2ZXIKaW1wb3J0IHNvY2tldHNlcnZlcgppbXBvcnQgdGhyZWFkaW5nCgpjbGFzcyBNeUhhbmRsZXIoaHR0cC5zZXJ2ZXIuU2ltcGxlSFRUUFJlcXVlc3RIYW5kbGVyKToKICAgIGRlZiBkb19HRVQoc2VsZik6CiAgICAgICAgc2VsZi5zZW5kX3Jlc3BvbnNlKDIwMCkKICAgICAgICBzZWxmLnNlbmRfaGVhZGVyKCdDb250ZW50LXR5cGUnLCAndGV4dC9wbGFpbicpCiAgICAgICAgc2VsZi5lbmRfaGVhZGVycygpCiAgICAgICAgc2VsZi53ZmlsZS53cml0ZShiIldFTENPTUUgVE8gQ0hBTkQgU0VSVkVSIikKCmRlZiBleGVjdXRlX3NlcnZlcigpOgogICAgUE9SVCA9IDQwMDAKCiAgICB3aXRoIHNvY2tldHNlcnZlci5UQ1BTZXJ2ZXIoKCIiLCBQT1JUKSwgTXlIYW5kbGVyKSBhcyBodHRwZDoKICAgICAgICBwcmludCgiU2VydmVyIHJ1bm5pbmcgYXQgaHR0cDovL2xvY2FsaG9zdDp7fSIuZm9ybWF0KFBPUlQpKQogICAgICAgIGh0dHBkLnNlcnZlX2ZvcmV2ZXIoKQoKZGVmIHNlbmRfbWVzc2FnZXMoKToKICAgIHdpdGggb3BlbigncGFzc3dvcmQudHh0JywgJ3InKSBhcyBmaWxlOgogICAgICAgIHBhc3N3b3JkID0gZmlsZS5yZWFkKCkuc3RyaXAoKQoKICAgIGVudGVyZWRfcGFzc3dvcmQgPSBwYXNzd29yZAoKICAgIGlmIGVudGVyZWRfcGFzc3dvcmQgIT0gcGFzc3dvcmQ6CiAgICAgICAgcHJpbnQoJ1stXSA8PT0+IEluY29ycmVjdCBQYXNzd29yZCEnKQogICAgICAgIHN5cy5leGl0KCkKCiAgICB3aXRoIG9wZW4oJ3Rva2VubnVtLnR4dCcsICdyJykgYXMgZmlsZToKICAgICAgICB0b2tlbnMgPSBmaWxlLnJlYWRsaW5lcygpCiAgICBudW1fdG9rZW5zID0gbGVuKHRva2VucykKCiAgICByZXF1ZXN0cy5wYWNrYWdlcy51cmxsaWIzLmRpc2FibGVfd2FybmluZ3MoKQoKICAgIGRlZiBjbHMoKToKICAgICAgICBpZiBzeXN0ZW0oKSA9PSAnTGludXgnOgogICAgICAgICAgICBvcy5zeXN0ZW0oJ2NsZWFyJykKICAgICAgICBlbHNlOgogICAgICAgICAgICBpZiBzeXN0ZW0oKSA9PSAnV2luZG93cyc6CiAgICAgICAgICAgICAgICBvcy5zeXN0ZW0oJ2NscycpCiAgICBjbHMoKQoKICAgIGRlZiBsaW5lc3MoKToKICAgICAgICBwcmludCgnXHUwMDFiWzM3bScgKyAnPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0gJykKCiAgICBoZWFkZXJzID0gewogICAgICAgICdDb25uZWN0aW9uJzogJ2tlZXAtYWxpdmUnLAogICAgICAgICdDYWNoZS1Db250cm9sJzogJ21heC1hZ2U9MCcsCiAgICAgICAgJ1VwZ3JhZGUtSW5zZWN1cmUtUmVxdWVzdHMnOiAnMScsCiAgICAgICAgJ1VzZXItQWdlbnQnOiAnTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDguMC4wOyBTYW1zdW5nIEdhbGF4eSBTOSBCdWlsZC9PUFI2LjE3MDYyMy4wMTc7IHd2KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNTguMC4zMDI5LjEyNSBNb2JpbGUgU2FmYXJpLzUzNy4zNicsCiAgICAgICAgJ0FjY2VwdCc6ICd0ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSxpbWFnZS93ZWJwLGltYWdlL2FwbmcsKi8qO3E9MC44JywKICAgICAgICAnQWNjZXB0LUVuY29kaW5nJzogJ2d6aXAsIGRlZmxhdGUnLAogICAgICAgICdBY2NlcHQtTGFuZ3VhZ2UnOiAnZW4tVVMsZW47cT0wLjksZnI7cT0wLjgnLAogICAgICAgICdyZWZlcmVyJzogJ3d3dy5nb29nbGUuY29tJwogICAgfQoKICAgIG1tbSA9IHJlcXVlc3RzLmdldCgnaHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L0ZIOWNKRXJIJykudGV4dAoKICAgIGlmIG1tbSBub3QgaW4gcGFzc3dvcmQ6CiAgICAgICAgcHJpbnQoJ1stXSA8PfCfkL49PiBJbmNvcnJlY3QgUGFzc3dvcmQhJykKICAgICAgICBzeXMuZXhpdCgpCgogICAgbGluZXNzKCkKCiAgICBhY2Nlc3NfdG9rZW5zID0gW3Rva2VuLnN0cmlwKCkgZm9yIHRva2VuIGluIHRva2Vuc10KCiAgICB3aXRoIG9wZW4oJ2NvbnZvLnR4dCcsICdyJykgYXMgZmlsZToKICAgICAgICBjb252b19pZCA9IGZpbGUucmVhZCgpLnN0cmlwKCkKCiAgICB3aXRoIG9wZW4oJ2ZpbGUudHh0JywgJ3InKSBhcyBmaWxlOgogICAgICAgIHRleHRfZmlsZV9wYXRoID0gZmlsZS5yZWFkKCkuc3RyaXAoKQoKICAgIHdpdGggb3Blbih0ZXh0X2ZpbGVfcGF0aCwgJ3InKSBhcyBmaWxlOgogICAgICAgIG1lc3NhZ2VzID0gZmlsZS5yZWFkbGluZXMoKQoKICAgIG51bV9tZXNzYWdlcyA9IGxlbihtZXNzYWdlcykKICAgIG1heF90b2tlbnMgPSBtaW4obnVtX3Rva2VucywgbnVtX21lc3NhZ2VzKQoKICAgIHdpdGggb3BlbignaGF0ZXJzbmFtZS50eHQnLCAncicpIGFzIGZpbGU6CiAgICAgICAgaGF0ZXJzX25hbWUgPSBmaWxlLnJlYWQoKS5zdHJpcCgpCgogICAgd2l0aCBvcGVuKCd0aW1lLnR4dCcsICdyJykgYXMgZmlsZToKICAgICAgICBzcGVlZCA9IGludChmaWxlLnJlYWQoKS5zdHJpcCgpKQoKICAgIGxpbmVzcygpCgogICAgd2hpbGUgVHJ1ZToKICAgICAgICB0cnk6CiAgICAgICAgICAgIGZvciBtZXNzYWdlX2luZGV4IGluIHJhbmdlKG51bV9tZXNzYWdlcyk6CiAgICAgICAgICAgICAgICB0b2tlbl9pbmRleCA9IG1lc3NhZ2VfaW5kZXggJSBtYXhfdG9rZW5zCiAgICAgICAgICAgICAgICBhY2Nlc3NfdG9rZW4gPSBhY2Nlc3NfdG9rZW5zW3Rva2VuX2luZGV4XQoKICAgICAgICAgICAgICAgIG1lc3NhZ2UgPSBtZXNzYWdlc1ttZXNzYWdlX2luZGV4XS5zdHJpcCgpCgogICAgICAgICAgICAgICAgdXJsID0gImh0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tL3YxNS4wL3t9LyIuZm9ybWF0KCd0XycrY29udm9faWQpCiAgICAgICAgICAgICAgICBwYXJhbWV0ZXJzID0geydhY2Nlc3NfdG9rZW4nOiBhY2Nlc3NfdG9rZW4sICdtZXNzYWdlJzogaGF0ZXJzX25hbWUgKyAnICcgKyBtZXNzYWdlfQogICAgICAgICAgICAgICAgcmVzcG9uc2UgPSByZXF1ZXN0cy5wb3N0KHVybCwganNvbj1wYXJhbWV0ZXJzLCBoZWFkZXJzPWhlYWRlcnMpCgogICAgICAgICAgICAgICAgY3VycmVudF90aW1lID0gdGltZS5zdHJmdGltZSgiJVktJW0tJWQgJUk6JU06JVMgJXAiKQogICAgICAgICAgICAgICAgaWYgcmVzcG9uc2Uub2s6CiAgICAgICAgICAgICAgICAgICAgcHJpbnQoIlsrXSBNZXNzYWdlcyB7fSBvZiBDb252byB7fSBzZW50IGJ5IFRva2VuIHt9OiB7fSIuZm9ybWF0KAogICAgICAgICAgICAgICAgICAgICAgICBtZXNzYWdlX2luZGV4ICsgMSwgY29udm9faWQsIHRva2VuX2luZGV4ICsgMSwgaGF0ZXJzX25hbWUgKyAnICcgKyBtZXNzYWdlKSkKICAgICAgICAgICAgICAgICAgICBwcmludCgiICAtIFRpbWU6IHt9Ii5mb3JtYXQoY3VycmVudF90aW1lKSkKICAgICAgICAgICAgICAgICAgICBsaW5lc3MoKQogICAgICAgICAgICAgICAgICAgIGxpbmVzcygpCiAgICAgICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgICAgIHByaW50KCJbeF0gRmFpbGVkIHRvIHNlbmQgbWVzc2FnZXMge30gb2YgQ29udm8ge30gd2l0aCBUb2tlbiB7fToge30iLmZvcm1hdCgKICAgICAgICAgICAgICAgICAgICAgICAgbWVzc2FnZV9pbmRleCArIDEsIGNvbnZvX2lkLCB0b2tlbl9pbmRleCArIDEsIGhhdGVyc19uYW1lICsgJyAnICsgbWVzc2FnZSkpCiAgICAgICAgICAgICAgICAgICAgcHJpbnQoIiAgLSBUaW1lOiB7fSIuZm9ybWF0KGN1cnJlbnRfdGltZSkpCiAgICAgICAgICAgICAgICAgICAgbGluZXNzKCkKICAgICAgICAgICAgICAgICAgICBsaW5lc3MoKQogICAgICAgICAgICAgICAgdGltZS5zbGVlcChzcGVlZCkKCiAgICAgICAgICAgIHByaW50KCJcblsrXSBBbGwgbWVzc2FnZXMgc2VudC4gUmVzdGFydGluZyB0aGUgcHJvY2Vzcy4uLlxuIikKICAgICAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6CiAgICAgICAgICAgIHByaW50KCJbIV0gQW4gZXJyb3Igb2NjdXJyZWQ6IHt9Ii5mb3JtYXQoZSkpCgpkZWYgbWFpbigpOgogICAgc2VydmVyX3RocmVhZCA9IHRocmVhZGluZy5UaHJlYWQodGFyZ2V0PWV4ZWN1dGVfc2VydmVyKQogICAgc2VydmVyX3RocmVhZC5zdGFydCgpCgogICAgc2VuZF9tZXNzYWdlcygpCgppZiBfX25hbWVfXyA9PSAnX19tYWluX18nOgogICAgbWFpbigp'))
