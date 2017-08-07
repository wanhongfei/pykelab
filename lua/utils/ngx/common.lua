--
-- Created by wanhongfei
-- User: 12727
-- Date: 2017/7/29
-- Time: 17:05
--

local _M = {}
_M.__VERSION = '0.0.1'

-- 获取url的参数，get和post都可获取
function _M.get_param(param_name)
    local arg = ngx.req.get_uri_args()
    if arg[param_name] ~= nil then
        return arg[param_name]
    end
    ngx.req.read_body() -- 解析 body 参数之前一定要先读取 body
    local arg = ngx.req.get_post_args()
    if arg[param_name] ~= nil then
        return arg[param_name]
    end
    return nil
end

-- 设置url参数,支持get和post的方法
-- set_by_lua_file $rw_request_uri 需要修改参数,lua层面不允许修改
-- function _M.set_param(param_name, param_value)
--    local method = _M:get_req_method()
--    local uri, args = _M:get_req_uri()
--    args[param_name] = param_value
--    return uri .. "?" .. ngx.encode_args(args)
-- end

-- 设置url参数
function _M.set_url_params(kv)
    local args = ngx.req.get_uri_args()
    for k, v in pairs(kv) do
        args[k] = v
    end
    ngx.req.set_uri_args(args)
end

-- 设置post的body参数，仅支持content-type=application/x-www-urlencoded
function _M.set_post_param(param_name, param_value)
    local method = _M:get_req_method()
    if method == 'POST' then
        local body = ngx.req.get_post_args();
        body[param_name] = param_value
        ngx.req.set_body_data(ngx.encode_args(body))
    end
end

-- 生成request_id,string类型
function _M.generate_req_id()
    -- 强迫nginx更新缓存获取最新的时间戳（毫秒级）
    ngx.update_time()
    return string.format("%s", ngx.now() * 1000)
end

-- 获取请求方法
function _M.get_req_method()
    return ngx.var.request_method
end

-- 获取客户端ip地址
function _M.get_client_ip()
    local headers = ngx.req.get_headers()
    return headers["X-REAL-IP"] or headers["X_FORWARDED_FOR"] or ngx.var.remote_addr or "0.0.0.0"
end

-- 获取请求uri和?xx=yy参数
function _M.get_req_uri()
    local req_uri = ngx.var.request_uri
    local pos, _ = string.find(req_uri, '?')
    if pos > 0 then
        local uri = string.sub(req_uri, 1, pos - 1)
        local args = ngx.decode_args(string.sub(req_uri, pos + 1))
        return uri, args
    else
        return req_uri, {}
    end
end

return _M
