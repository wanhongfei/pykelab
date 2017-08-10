--
-- Created by IntelliJ IDEA.
-- User: 12727
-- Date: 2017/7/29
-- Time: 17:14
-- To change this template use File | Settings | File Templates.
--
package.path = package.path .. ';D:\\workspace\\pykelab_vf\\lua\\?.lua';
local common = require 'ngx.utils.common'
ngx.say(common:get_param('a'))

local uri = common:set_param('b', '222')
ngx.say(uri)

ngx.say(common:generate_req_id())
