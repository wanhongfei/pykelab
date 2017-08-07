local _M = {}
_M.__VERSION = '0.0.1'

-- 2 -> 16
function _M.bin_2_hex(str)
    return string.gsub(str, "(.)", function(x)
        return string.format("%02x", string.byte(x))
    end)
end

return _M