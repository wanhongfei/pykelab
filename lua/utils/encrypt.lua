---
--- Created by wanhongfei.
--- DateTime: 2017/8/7 上午10:35
---
local resty_sha1 = require "resty.sha1"
local resty_md5 = require "resty.md5"
local resty_str = require "resty.string"

local _M = {}
_M.__VERSION = '0.0.1'

-- md5_bin
function _M.md5(str)
    return md5_core.sum(str)
end

-- sha1_hex
function _M.sha1_hex(str)
    local sha1 = resty_sha1:new()
    sha1:update(str)
    local digest = sha1:final()
    return resty_str.to_hex(digest)
end

-- md5_hex
function _M.md5_hex(str)
    local md5 = resty_md5:new()
    md5:update(str)
    local digest = md5:final()
    return resty_str.to_hex(digest)
end

return _M