from regression import *

__doc__ = """
>>> t = Table(bill)
>>> print pretty_html(t.render())
<tbody>
 <tr>
  <td class="table_label">
   Email:
  </td>
  <td class="table_field">
   bill@example.com
  </td>
 </tr>
 <tr>
  <td class="table_label">
   Password:
  </td>
  <td class="table_field">
   1234
  </td>
 </tr>
 <tr>
  <td class="table_label">
   Name:
  </td>
  <td class="table_field">
   Bill
  </td>
 </tr>
 <tr>
  <td class="table_label">
   Orders:
  </td>
  <td class="table_field">
   Quantity: 10
  </td>
 </tr>
</tbody>

>>> t = TableCollection(User, [bill])
>>> print pretty_html(t.render().strip())
<thead>
 <tr>
  <th>
   Email:
  </th>
  <th>
   Password:
  </th>
  <th>
   Name:
  </th>
  <th>
   Orders:
  </th>
 </tr>
</thead>
<tbody>
 <tr>
  <td>
   bill@example.com
  </td>
  <td>
   1234
  </td>
  <td>
   Bill
  </td>
  <td>
   Quantity: 10
  </td>
 </tr>
</tbody>
"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()