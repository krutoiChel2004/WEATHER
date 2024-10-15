import { Table } from 'antd';

const TableLog = ({ dataState, loading }) => {
  const columns = [
    {
      title: 'Temperature (°C)',
      dataIndex: 'temperature',
      key: 'temperature',
    },
    {
      title: 'Weather Description',
      dataIndex: 'weather_code_description',
      key: 'weather_code_description',
    },
    {
      title: 'Precipitation (mm)',
      dataIndex: 'precipitation',
      key: 'precipitation',
    },
    {
      title: 'Surface Pressure (hPa)',
      dataIndex: 'surface_pressure',
      key: 'surface_pressure',
    },
    {
      title: 'Wind Speed (m/s)',
      dataIndex: 'wind_speed_10m',
      key: 'wind_speed_10m',
    },
    {
      title: 'Wind Direction (°)',
      dataIndex: 'wind_direction_10m',
      key: 'wind_direction_10m',
    },
    {
      title: 'Wind Direction Description',
      dataIndex: 'wind_direction_description',
      key: 'wind_direction_description',
    },
    {
      title: 'Time (Moscow)',
      dataIndex: 'time_moscow',
      key: 'time_moscow',
    },
  ];

  const enhancedData = dataState.map((item, index) => ({ ...item, key: `${item.time_moscow}-${index}` }));

  return (
    <Table
      columns={columns}
      dataSource={enhancedData} 
      loading={loading}
      rowKey="key" 
    />
  );
};

export default TableLog;
