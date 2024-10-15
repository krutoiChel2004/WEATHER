import { DatePicker, Space } from 'antd';

const { RangePicker } = DatePicker;
const dateFormat = 'DD/MM/YYYY';

const DatePicker_ = ({ onChange }) => (
  <Space direction="vertical">
    <RangePicker onChange={onChange} format={dateFormat} style={{ margin: 10 }} /> {/* RangePicker for start and end date */}
  </Space>
);

export default DatePicker_;
