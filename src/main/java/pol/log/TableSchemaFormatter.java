package pol.log;

import pol.db.Column;
import pol.db.Table;

/**
 * 
 * @author Joon-Seok Kim (jkim258 at gmu.edu)
 * 
 */
public class TableSchemaFormatter extends AbstractFormatter {
	private static final long serialVersionUID = 1852254379797589470L;

	@Override
	protected String format(Object value) {
		Table table = null;
		if (value instanceof Table) {
			table = (Table) value;
		} else if (value instanceof TableMapper) {
			table = ((TableMapper) value).getTable();
		}

		if (table != null) {
			StringBuilder sb = new StringBuilder();
			Column[] columns = table.getColumns();
			for (int i = 0; i < columns.length; i++) {
				sb.append(columns[i].name).append("\t");
			}
			sb.deleteCharAt(sb.length() - 1);
			return sb.toString();
		}
		throw new RuntimeException("The value must be either " + Table.class + " or " + TableMapper.class + ".");
	}
}