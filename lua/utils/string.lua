local _M = {}
_M.__VERSION = '0.0.1'

-- 检查是否为空
function _M.is_empty(str)
    return str == nil or #str == 0
end

return _M
