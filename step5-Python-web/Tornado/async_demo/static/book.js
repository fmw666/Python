$(function() {
    // 删除
    $('.del').on('click', function() {
        result = $(this).siblings().eq(0).children('input').val()
        $.ajax({
            url: '/',
            dataType: 'json',
            type: 'delete',
            data: JSON.stringify({id: result}),
            success: function(dat) {
                alert(dat.data)
                $(this).parent().remove()
                console.log($(this))
                window.location.reload()
            }
        })
    })

    // 更新
    $('.update').on('click', function() {
        var upTds = $(this).siblings()
        dict_data = {}
        for (var i=0; i<(upTds.length-1); i++) {
            if (i == 0) {
                dict_data.bid = upTds.eq(i).children('input').val()
            } else if (i == 1) {
                dict_data.btitle = upTds.eq(i).children('input').val()
            } else if (i == 2) {
                dict_data.bauthor = upTds.eq(i).children('input').val()
            } else if (i == 3) {
                dict_data.bperson = upTds.eq(i).children('input').val()
            } else if (i == 4) {
                dict_data.bpub_date = upTds.eq(i).children('input').val()
            } else if (i == 5) {
                dict_data.bread = upTds.eq(i).children('input').val()
            } else if (i == 6) {
                dict_data.bcomment = upTds.eq(i).children('input').val()
            }
        }
        if (dict_data.bid == "" | dict_data.btitle == "" | dict_data.bauthor == "" | dict_data.bperson == "" | dict_data.bpub_date == "" | dict_data.bread == "" | dict_data.bcomment == "") {
            alert('输入内容不能为空！')
            return
        }
        $.ajax({
            url: '/',
            dataType: 'json',
            type: 'put',
            data: dict_data,
            success: function(dat) {
                alert(dat.data)
                window.location.reload()
            }
        })
    })

    // 增添
    $('.add').on('click', function() {
        var addTds = $('.addlist input')
        dict_data = {}
        for (var i=0; i<(addTds.length-1); i++) {
            if (i == 0) {
                dict_data.btitle = addTds.eq(i).val()
            } else if (i == 1) {
                dict_data.bauthor = addTds.eq(i).val()
            } else if (i == 2) {
                dict_data.bperson = addTds.eq(i).val()
            } else if (i == 3) {
                dict_data.bpub_date = addTds.eq(i).val()
            } else if (i == 4) {
                dict_data.bread = addTds.eq(i).val()
            } else if (i == 5) {
                dict_data.bcomment = addTds.eq(i).val()
            }
        }
        if (dict_data.btitle == "" | dict_data.bauthor == "" | dict_data.bperson == "" | dict_data.bpub_date == "" | dict_data.bread == "" | dict_data.bcomment == "") {
            alert('输入内容不能为空！')
            return
        }
        $.post({
            url: '/',
            dataType: 'json',
            data: dict_data,
            success: function(dat) {
                alert(dat.data)
                window.location.reload()
                // 清空所有输入框
                for (var i=0; i<(addTds.length-1); i++) {
                    console.log(i)
                    addTds.eq(i).val("")
                }
            }
        })
    })
})