// src/utils/params.ts
import type { CollectionEntry } from 'astro:content';

export function getBlogParams(post: CollectionEntry<'blog'>) {
  // Grab the `pubDate` from the blog post's frontmatter.
  // This will be of type `Date`, since the `CollectionEntry` of type 'blog'
  // defines the `pubDate` field as type 'Date'.
  const pubDate = post.data.pubDate;

  // Parse out the year, month and day from the `pubDate`.
  const pubYear = String(pubDate.getFullYear()).padStart(4, '0');
  const pubMonth = String(pubDate.getMonth() + 1).padStart(2, '0');
  const pubDay = String(pubDate.getDate()).padStart(2, '0');

  // Astro generates the `slug` from the filename of the content.
  // Our filenames begin with `YYYY-MM-DD-`, but we don't want this in our resulting URL.
  // So, we use a regex to remove this prefix, if it exists.
  const slug =
    (post.id.match(/\d{4}-\d{2}-\d{2}_(.+)/) || [])[1] || post.id;

  // Build our desired date-based path from the relevant parts.
  const path = `${pubYear}/${pubMonth}/${pubDay}/${slug}`;

  // Return each token so it can be used by calling code.
  return {
    year: pubYear,
    month: pubMonth,
    day: pubDay,
    path,
    slug,
  };
}