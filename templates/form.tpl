{# form.tpl フォーム #}
<div>
	<form action="/update" method="post" id="update">
		<label>id: <input type="text" name="id" placeholder="id"></label>
		<label>tag: <input type="text" name="tags" placeholder="tag1[, tag2, ...])"></label>
		<label>detail: <input type="text" name="detail" placeholder="detail"></label>
		<input type = "hidden" name="mode" value = "{{ tmpl_mode }}" />
		<input type = "hidden" name="mode_value" value = "{{ tmpl_mode_value }}" />
		<input type = "submit" value = "submit" />
	</form>
</div>