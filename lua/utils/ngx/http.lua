local _M = {}
_M.__VERSION = '0.0.1'

-- get请求指定url，并获取response
function _M.get(url)
    local res = ngx.location.capture(url)
    if res.status == 200 then
        return res.body
    end
    return nil
end

-- post请求指定url，并获取response
function _M.post(url,body)
    local res = ngx.location.capture(url,{method=ngx.HTTP_POST, body=body})
    if res.status == 200 then
        return res.body
    end
    return nil
end

return _M
