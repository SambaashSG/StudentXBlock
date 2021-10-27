/* Javascript for StudentXBlock. */
function StudentXBlock(runtime, element) {
  $(element).find('.action-cancel').bind('click', function(){
    runtime.notify('cancel', {});
  });
  $(element).find('.action-save').bind('click', function(){
    var data = {
      'display_name': $("#edit_display_name").val(),
      'host_url': $("#edit_host_url").val(),
      'btn_text': $("#btn_edit_text").val()
    };
    runtime.notify('save', {state:'start'})
    var handleUrl = runtime.handlerUrl(element, 'save_student_value');
    $.post(handleUrl, JSON.stringify(data)).done(function(response){
      if(response.result == 'success'){
        runtime.notify('save',{state:'end'});
      }else{
        runtime.notify('error', {msg: response.message})
      }
    });
  });
}
