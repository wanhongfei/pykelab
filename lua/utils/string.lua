local _M = {}
_M.__VERSION = '0.0.1'

-- 检查是否为空
function _M.is_empty(str)
    return str == nil or #str == 0
end

-- lower
function _M.lower(str)
    return string.lower(str)
end

-- upper
function _M.upper(str)
    return string.upper(str)
end

-- sub string [left,right] 0,2
function _M.sub(str, left, right)
    if left >= 0 and left <= #str - 1 and right >= left and right <= #str - 1 then
        return string.sub(left + 1, right + 1)
    else
        return nil
    end
end

-- check startwith
function _M.startwith(str, prefix)
    return sub(str, 1, #prefix) == prefix
end

-- check endwith
function _M.endwith(str, suffix)
    return sub(str, #str - #suffix, #str) == suffix
end

--format
function _M.format(str, ...)
    return string.format(str, ...)
end

return _M
